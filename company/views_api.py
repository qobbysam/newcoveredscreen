from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework.generics import UpdateAPIView

from .models import UserCompanyModel
from .serializers import UserCompanyModelSerializer
# Create your views here.


class UpdateCompanyAPIView(UpdateAPIView):
    queryset = UserCompanyModel.objects.all()
    serializer_class = UserCompanyModelSerializer
