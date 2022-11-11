from django.urls import path

from userpublic.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage' ),
    #path('', RedirectView.as_view(url='/home/')),
]