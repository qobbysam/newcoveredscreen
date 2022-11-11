

from django.urls import path
from .views import UpdateCompanyView
urlpatterns = [
    path('edit-company/<int:pk>', UpdateCompanyView.as_view(), name='gen-company-edit')
]
