from django.contrib.auth.decorators import login_required
from django.urls import path, include , re_path

from drugtest import views

urlpatterns = [
    path('alldrugtest/', views.DrugTestListView.as_view(), name='gen-drugtests' ),
    path('viewdrugtest/<int:pk>', views.ViewOneDrugTest.as_view(), name='gen-drugtest-one'),
    path('search-locations/', views.searchApiView, name='gen-drugtest-search-location'  )

]