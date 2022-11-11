from datetime import date
from django.shortcuts import render
from django import http
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.conf import settings
import logging
from oscar.apps.checkout.mixins import OrderPlacementMixin

from oscar.apps.checkout import signals
from oscar.apps.payment import forms, models

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from oscar.core.loading import get_classes, get_class
from squarepayment.errcodes import IDEMPOTENCY_KEY_REUSED
from squarepayment.facade import Facade
from squarepayment.interface import Result

from squarepayment.serializers import PaynowSerializer

RedirectRequired, UnableToTakePayment, PaymentError \
    = get_classes('payment.exceptions', ['RedirectRequired',
                                         'UnableToTakePayment',
                                         'PaymentError'])
UnableToPlaceOrder = get_class('order.exceptions', 'UnableToPlaceOrder')
SurchargeApplicator = get_class("checkout.applicator", "SurchargeApplicator")
CheckoutSessionData = get_class(
    'checkout.utils', 'CheckoutSessionData')
Repository = get_class('shipping.repository', 'Repository')

OrderTotalCalculator = get_class(
    'checkout.calculators', 'OrderTotalCalculator')

logger = logging.getLogger('oscar.checkout')

# Create your views here.


class Paynow(OrderPlacementMixin, APIView):

    # authentication_classes

    def post(self, request, *args, **kwargs):
        serializer = PaynowSerializer(data=request.data)
        if serializer.is_valid():
            # msg_out = serializer.save_msg(request.user)
            token = serializer.data['token']

            return self.do_place_order(request, token, *args, **kwargs)
            # return Response(msg_out['body'], status=msg_out['status'])
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            errs = serializer.errors

            return Response(errs, status=status_code)

    def do_place_order(self, request, token, *args, **kwargs):

        submission = self.build_submission(*args, **kwargs)

        self.checkout_session = CheckoutSessionData(self.request)
        
        basket = submission['basket']

        print(self.checkout_session.shipping_method_code(basket))

        shipping_address=submission['shipping_address']

        shipping_method = self.get_shipping_method(
            basket, shipping_address)

        if not shipping_method:
            total = shipping_charge = surcharges = None
        else:
            shipping_charge = shipping_method.calculate(basket)
            surcharges = SurchargeApplicator(self.request, submission).get_applicable_surcharges(
                self.request.basket, shipping_charge=shipping_charge
            )
            total = self.get_order_totals(
                basket, shipping_charge=shipping_charge, surcharges=surcharges, **kwargs)

        submission["shipping_charge"] = shipping_charge
        submission["order_total"] = total
        submission['surcharges'] = surcharges

        # If there is a billing address, add it to the payment kwargs as calls
        # to payment gateways generally require the billing address. Note, that
        # it normally makes sense to pass the form instance that captures the
        # billing address information. That way, if payment fails, you can
        # render bound forms in the template to make re-submission easier.
     
        # Allow overrides to be passed in
        #submission.update(kwargs)

        # Set guest email after overrides as we need to update the order_kwargs
        # entry.
        user = submission['user']
        if (not user.is_authenticated
                and 'guest_email' not in submission['order_kwargs']):
            email = self.checkout_session.get_guest_email()
            submission['order_kwargs']['guest_email'] = email
        # submission['shipping_method'] = ''
        # submission['shipping_charge'] = self.get_shipping_method(submission['basket'])
        # submission['order_total'] = ''

        


        submission['payment_kwargs']['token'] = token

        print(submission)

        return self.submit(**submission)


    def get_shipping_method(self, basket, shipping_address=None, **kwargs):
            """
            Return the selected shipping method instance from this checkout session

            The shipping address is passed as we need to check that the method
            stored in the session is still valid for the shipping address.
            """
            code = self.checkout_session.shipping_method_code(basket)
            methods = Repository().get_shipping_methods(
                basket=basket, user=self.request.user,
                shipping_addr=shipping_address, request=self.request)
            for method in methods:
                if method.code == code:
                    return method
    def get_order_totals(self, basket, shipping_charge, surcharges=None, **kwargs):
        """
        Returns the total for the order with and without tax
        """
        return OrderTotalCalculator(self.request).calculate(
            basket, shipping_charge, surcharges, **kwargs)

    # def handle_place_order_submission(self, request):
    #     """
    #     Handle a request to place an order.

    #     This method is normally called after the customer has clicked "place
    #     order" on the preview page. It's responsible for (re-)validating any
    #     form information then building the submission dict to pass to the
    #     `submit` method.

    #     If forms are submitted on your payment details view, you should
    #     override this method to ensure they are valid before extracting their
    #     data into the submission dict and passing it onto `submit`.

    #     """
    #     return self.submit(**self.build_submission())

    def handle_payment(self, order_number, total, **kwargs):
        token = kwargs['token']
        #billing_add = kwargs['billing_address']
        idempotency = str(order_number) + str(date.today())
        total_ = total.incl_tax
        amount = float(total_)
        #print(dir(total))
        #print(dir(amount))

        facade = Facade()

        result = facade.authorize(token,amount,idempotency)

        res_obj = Result(result, order_number)

        if res_obj.isSuccess():

            #body = res_obj.buildsuccessMsg()
            source_type, is_created = models.SourceType.objects.get_or_create(
            name='squarepayment')
            source = source_type.sources.model(
                source_type=source_type,
                amount_allocated=total.incl_tax, currency=total.currency)
            self.add_payment_source(source)
            self.add_payment_event('Authorised', total.incl_tax)
        else:

            errors = res_obj.serialize_errors()

            for err in errors:

               if  err['code'] == IDEMPOTENCY_KEY_REUSED:
                raise PaymentError

            raise UnableToTakePayment

        

    def submit(self, user, basket, shipping_address, shipping_method,  # noqa (too complex (10))
               shipping_charge, billing_address, order_total,
               payment_kwargs=None, order_kwargs=None, surcharges=None):
        """
        Submit a basket for order placement.

        The process runs as follows:

         * Generate an order number
         * Freeze the basket so it cannot be modified any more (important when
           redirecting the user to another site for payment as it prevents the
           basket being manipulated during the payment process).
         * Attempt to take payment for the order
           - If payment is successful, place the order
           - If a redirect is required (e.g. PayPal, 3D Secure), redirect
           - If payment is unsuccessful, show an appropriate error message

        :basket: The basket to submit.
        :payment_kwargs: Additional kwargs to pass to the handle_payment
                         method. It normally makes sense to pass form
                         instances (rather than model instances) so that the
                         forms can be re-rendered correctly if payment fails.
        :order_kwargs: Additional kwargs to pass to the place_order method
        """
        if payment_kwargs is None:
            payment_kwargs = {}
        if order_kwargs is None:
            order_kwargs = {}

        # Taxes must be known at this point
        assert basket.is_tax_known, (
            "Basket tax must be set before a user can place an order")
        assert shipping_charge.is_tax_known, (
            "Shipping charge tax must be set before a user can place an order")

        # We generate the order number first as this will be used
        # in payment requests (ie before the order model has been
        # created).  We also save it in the session for multi-stage
        # checkouts (e.g. where we redirect to a 3rd party site and place
        # the order on a different request).
        order_number = self.generate_order_number(basket)
        self.checkout_session.set_order_number(order_number)
        logger.info("Order #%s: beginning submission process for basket #%d",
                    order_number, basket.id)

        # Freeze the basket so it cannot be manipulated while the customer is
        # completing payment on a 3rd party site.  Also, store a reference to
        # the basket in the session so that we know which basket to thaw if we
        # get an unsuccessful payment response when redirecting to a 3rd party
        # site.
        self.freeze_basket(basket)
        self.checkout_session.set_submitted_basket(basket)

        # We define a general error message for when an unanticipated payment
        # error occurs.
        error_msg = _("A problem occurred while processing payment for this "
                      "order - no payment has been taken.  Please "
                      "contact customer services if this problem persists")

        signals.pre_payment.send_robust(sender=self, view=self)

        try:
            self.handle_payment(order_number, order_total, **payment_kwargs)
        except RedirectRequired as e:
            # Redirect required (e.g. PayPal, 3DS)
            logger.info("Order #%s: redirecting to %s", order_number, e.url)
            return http.HttpResponseRedirect(e.url)
        except UnableToTakePayment as e:
            # Something went wrong with payment but in an anticipated way.  Eg
            # their bankcard has expired, wrong card number - that kind of
            # thing. This type of exception is supposed to set a friendly error
            # message that makes sense to the customer.
            msg = str(e)
            logger.warning(
                "Order #%s: unable to take payment (%s) - restoring basket",
                order_number, msg)
            self.restore_frozen_basket()

            # We assume that the details submitted on the payment details view
            # were invalid (e.g. expired bankcard).
            return self.render_payment_details_api(
                self.request, error=msg, **payment_kwargs)

        except PaymentError as e:
            # A general payment error - Something went wrong which wasn't
            # anticipated.  Eg, the payment gateway is down (it happens), your
            # credentials are wrong - that king of thing.
            # It makes sense to configure the checkout logger to
            # mail admins on an error as this issue warrants some further
            # investigation.
            msg = str(e)
            logger.error("Order #%s: payment error (%s)", order_number, msg,
                         exc_info=True)
            self.restore_frozen_basket()
            return self.render_preview_api(
                self.request, error=error_msg, **payment_kwargs)
        except Exception as e:
            # Unhandled exception - hopefully, you will only ever see this in
            # development...
            logger.exception(
                "Order #%s: unhandled exception while taking payment (%s)",
                order_number, e)
            self.restore_frozen_basket()
            return self.render_preview(
                self.request, error=error_msg, **payment_kwargs)

        signals.post_payment.send_robust(sender=self, view=self)

        # If all is ok with payment, try and place order
        logger.info("Order #%s: payment successful, placing order",
                    order_number)
        try:
            #response = self.
            response = self.handle_order_placement(
                order_number, user, basket, shipping_address, shipping_method,
                shipping_charge, billing_address, order_total, surcharges=surcharges, **order_kwargs)

            return self.success_response(response, order_number)
        except UnableToPlaceOrder as e:
            # It's possible that something will go wrong while trying to
            # actually place an order.  Not a good situation to be in as a
            # payment transaction may already have taken place, but needs
            # to be handled gracefully.
            msg = str(e)
            logger.error("Order #%s: unable to place order - %s",
                         order_number, msg, exc_info=True)
            self.restore_frozen_basket()
            return self.render_preview_api(
                self.request, error=msg, **payment_kwargs)
        except Exception as e:
            # Hopefully you only ever reach this in development
            logger.exception("Order #%s: unhandled exception while placing order (%s)", order_number, e)
            error_msg = _("A problem occurred while placing this order. Please contact customer services.")
            self.restore_frozen_basket()
            return self.render_preview_api(self.request, error=error_msg, **payment_kwargs)


    def render_preview_api(self, request, error, **payment_kwargs):
        msg = {}
        msg['error'] = error
        status_code = status.HTTP_400_BAD_REQUEST
        return Response(msg, status=status_code)

    def render_payment_details_api(self,request, error,**payment_kwargs):
        msg = {}
        msg['error'] = error
        status_code = status.HTTP_400_BAD_REQUEST
        return Response(msg, status=status_code)

    def success_response(self,response, order_number,**payment_kwargs):
        status_code = status.HTTP_201_CREATED
        msg_out = {}
        msg_out['thankurl'] = reverse('checkout:thank-you')
        msg_out['order_number'] = order_number
        return Response(msg_out, status= status_code)

