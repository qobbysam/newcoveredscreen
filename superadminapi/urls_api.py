from django.urls import path, include, re_path

from rest_auth.views import LogoutView
from superadminapi import view_api
from oscarapi.urls import admin_urlpatterns

urlpatterns = [

    path("oscar/", include(admin_urlpatterns)),
    path("login-office/", view_api.OfficeLoginView.as_view(), name="admin-api-office-login"),
    path("login-admin/", view_api.AdminLoginView.as_view(), name="admin-api-admin-login"),

    path("logout/", LogoutView.as_view(), name="admin-api-logout"),
    path("user/", view_api.UserDetail.as_view(), name="admin-api-user-office"),

    path("status-quest/", view_api.StatusQuestAPIView.as_view(), name="admin-api-status-quest"),
    path("search-orders/", view_api.SearchOrdersAPIView.as_view(), name="admin-api-search-orders"),
    path("search-drugtest/", view_api.SearchDrugtestAPIView.as_view(), name="admin-api-search-drugtest"),
    
    # path("one-drugtest/<int:pk>/", view_api.DrugtestAPIView.as_view(), name="admin-api-drugtest"),                        ) 
]
