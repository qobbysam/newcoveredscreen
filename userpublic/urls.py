from django.urls import path

from userpublic.views import HomePageView, OfficeAdminView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage' ),
    path('officeadmin/', OfficeAdminView.as_view(), name="office-admin-homepage" )
    #path('', RedirectView.as_view(url='/home/')),
]