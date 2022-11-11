from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import  UpdateView

from .models import UserCompanyModel
from .forms import UpdateCompanyForm
# Create your views here.


class UpdateCompanyView(UpdateView):
    template_name = 'company/update.html'
    form_class = UpdateCompanyForm
    success_url = reverse_lazy('customer:profile-view')
    model = UserCompanyModel
