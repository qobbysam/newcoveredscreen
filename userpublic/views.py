from django.views.generic.base import TemplateView



class HomePageView(TemplateView):

    template_name = "userpublic/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_context'] = "message from testing context"
        return context
    

class OfficeAdminView(TemplateView):

    template_name = "userpublic/adminindex.html"