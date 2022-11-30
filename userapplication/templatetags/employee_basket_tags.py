import json
from django import template
from django.urls import reverse
from oscar.core.loading import get_class, get_model
from django.conf import settings
AddToBasketForm = get_class('basket.forms', 'AddToBasketForm')
SimpleAddToBasketForm = get_class('basket.forms', 'SimpleAddToBasketForm')
Product = get_model('catalogue', 'product')

register = template.Library()

QNT_SINGLE, QNT_MULTIPLE = 'single', 'multiple'


@register.simple_tag
def employee_basket_object(request, product ,quantity_type='single'):
    if not isinstance(product, Product):
        return ''

    initial = {}
    if not product.is_parent:
        initial['product_id'] = product.id

    form_class = AddToBasketForm
    if quantity_type == QNT_SINGLE:
        form_class = SimpleAddToBasketForm

    form = form_class(request.basket, product=product, initial=initial)

    json_object = buildjson(request=request, product=product)
    
    return json.dumps(json_object)


def buildjson(request, product):

    obj = {}

    obj['is_drug_test'] = True
    obj['mes'] = "called from context"
    obj['product'] = product.id
    obj['searchurl'] = settings.SITE_BASE_URL
    obj['paymenturl'] = reverse('checkout:preview')
   
    #obj['options'] = product.

    return obj
