from django import template

from wagtail.core.models import Page, Site


from service.models import  ServiceIndexPage

register = template.Library()

@register.simple_tag(takes_context=True)
def services(context):
    #self = context.get('self')
    request = context.get("request")

    service_index = ServiceIndexPage.objects.live().first()

    #services = ServiceIndexPage.get_context(request)

    services = service_index.get_context(request=request)
    #services = service_index.get_services()
    return services

    # if self is None:
    #     live_service = Page.objects.get(ServiceIndexPage).live()
    #     services =  ServiceIndexPage.get_context(live_service,request=request)
    #     print("calling in first")
    #     return services
    # else:

    #     #returns a dictionary of services
    #     services =  ServiceIndexPage.get_context(self=self,request=request)
    #     print ("calling in second")
    #     return services

@register.filter()
def truncate_service(value, args):
    out = value.split()[:int(args)]
    return " ".join(out)
