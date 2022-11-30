from django import template
from django.urls import reverse
from company.models import UserCompanyModel

register = template.Library()

@register.simple_tag
def user_company_object(request):

    current_company = UserCompanyModel.objects.get(pk = request.user.default_company)

    return current_company
