from unicodedata import name
from django.contrib.auth.decorators import login_required
from django.urls import path, include , re_path

from employee import views_api

urlpatterns = [
    path('allemployee/', views_api.EmployeeListAPIView.as_view(), name='gen-employees' ),
    path('newemployee/', views_api.EmployeeCreateAPIView.as_view(), name='gen-employee-create'),
    path('employee/<int:pk>', views_api.EmployeeRetrieveUpdateDeleteAPIView.as_view(), name='gen-employee-one'),
    #path('editemployee/<int:pk>', views.EmployeeUpdateView.as_view(), name='gen-employee-edit'),
    #path('deleteemployee/<int:pk>', views.EmployeeDeleteView.as_view(), name='gen-employee-delete'),
    
    path('toggle/active/<int:pk>', views_api.EmployeeToggleAPIView.as_view(), name='gen-employee-toggle'),
    #path('download/active/', views.EmployeeDownloadActive.as_view(), name='gen-employee-download-active')



]