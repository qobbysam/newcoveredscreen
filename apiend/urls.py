from django.apps import apps
from django.urls import path,include, re_path
from rest_framework import routers
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from allauth.account.views import confirm_email


#from apiend.views import UserViewSet, UserInfoViewset
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (such as pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)


# ViewSets define the view behavior.


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, 'user-auth')
# router.register(r'get-info', UserInfoViewset, basename='user-info')



urlpatterns = [
    

    path('wagtail/', api_router.urls ),

    path ('userapp/', include(router.urls)),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),

    #path('salesman/', include('salesman.urls')),
    path("oscar/", include(apps.get_app_config("oscarapicheckout").urls[0])),
    path("oscar/", include("oscarapi.urls")),

    path('sqapi/', include('squarepayment.urls')) 
    


    # Ensure that the api_router line appears above the default Wagtail page serving route
    
]