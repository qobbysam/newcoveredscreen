from django.contrib.auth.decorators import login_required
from django.urls import path, include , re_path

from squarepayment import views

urlpatterns = [
    path('squarepaynow/', views.Paynow.as_view(), name='gen-paynow-square' ),


]