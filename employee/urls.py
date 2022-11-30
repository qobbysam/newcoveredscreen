from unicodedata import name
from django.contrib.auth.decorators import login_required
from django.urls import path, include , re_path

from employee import views

urlpatterns = [
    path('allemployee/', views.EmployeeListView.as_view(), name='gen-employees' ),
    path('newemployee/', views.EmployeeCreateView.as_view(), name='gen-employee-create'),
    path('viewemployee/<int:pk>', views.EmployeeListView.as_view(), name='gen-employee-one'),
    path('editemployee/<int:pk>', views.EmployeeUpdateView.as_view(), name='gen-employee-edit'),
    path('deleteemployee/<int:pk>', views.EmployeeDeleteView.as_view(), name='gen-employee-delete'),
    path('toggle/active/<int:pk>', views.EmployeeToggleView.as_view(), name='gen-employee-toggle'),
    path('download/active/', views.EmployeeDownloadActive.as_view(), name='gen-employee-download-active')



]