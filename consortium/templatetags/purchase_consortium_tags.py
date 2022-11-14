from django import template

from consortium.models import ConsortiumModel

register = template.Library()

@register.simple_tag(takes_context=True)
def can_purchase_consortium(context):
    request = context.get("request")

    company = request.user.default_company

    consortium = ConsortiumModel.objects.get(pk = company)
    return consortium.can_purchase()
    
