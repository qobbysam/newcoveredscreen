from django.contrib.auth.decorators import login_required
from django.urls import path, include , re_path

from drugtest import views_api

urlpatterns = [
    path('alldrugtest/', views_api.DrugTestListAPIView.as_view(), name='api-drugtests' ),
    path('viewdrugtest/<int:pk>', views_api.ViewOneDrugTestAPIView.as_view(), name='api-drugtest-one'),
    path('search-locations/', views_api.searchApiView, name='api-drugtest-search-location'  )

]