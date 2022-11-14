from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def select_template_object(request):

    if request.user.is_authenticated():

        return 'oscar/layout_2_col_account.html'
    else:
        return 'oscar/layout.html'
