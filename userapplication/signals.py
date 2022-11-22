from django.dispatch import Signal, receiver

from oscar.apps.order.signals import order_placed

from userapplication.orderhandler import OrderHandler

@receiver(order_placed)
def order_placed_receiver(sender, user, order , **kwargs):
    print("receiver called")
    # print(order)

    if order.status == 'Authorized':

        received_order = OrderHandler(order, user,sender)

        received_order.handle(sender)

            


def async_caller(user,order):
    from django_q.tasks import async_task, result
    from userapplication.tasks import employee_creator

    async_task(employee_creator, user,order)

    ##send category create signal






