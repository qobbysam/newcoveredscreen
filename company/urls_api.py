

from django.urls import path
from .views_api import UpdateCompanyAPIView


urlpatterns = [
    path('edit-company/<int:pk>', UpdateCompanyAPIView.as_view(), name='api-company-edit')
]
