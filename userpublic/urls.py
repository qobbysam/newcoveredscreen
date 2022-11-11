from django.urls import path

from userpublic.views import HomePageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='homepage' ),
]