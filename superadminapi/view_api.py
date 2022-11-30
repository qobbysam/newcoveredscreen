
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from oscar.apps.customer.signals import user_registered
from oscar.core.loading import get_class, get_model

from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from oscarapi.utils.loading import get_api_classes
from oscarapi.basket import operations


LoginSerializer, UserSerializer, RegisterUserSerializer = get_api_classes(
    "serializers.login", ["LoginSerializer", "UserSerializer", "RegisterUserSerializer"]
)
RegisterUserMixin = get_class("customer.mixins", "RegisterUserMixin")

Basket = get_model("basket", "Basket")
User = get_user_model()

__all__ = ("LoginView", "UserDetail")


class AdminLoginView(APIView):
    """
    Api for logging in users.

    DELETE:
    Log the user out by destroying the session.
    Anonymous users will have their cart destroyed as well, because there is
    no way to reach it anymore

    POST(username, password):
    1. The user will be authenticated. The next steps will only be
       performed is login is successful. Logging in logged in users results in
       405.

    GET:

    """

    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if getattr(settings, "OSCARAPI_EXPOSE_USER_DETAILS", False):
                ser = UserSerializer(request.user, many=False)
                return Response(ser.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise MethodNotAllowed("GET")


    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data)
        
        if ser.is_valid():

            print(ser.instance)
            
            # refuse to login logged in users, to avoid attaching sessions to
            # multiple users at the same time.
            if request.user.is_authenticated:
                if request.user.is_superuser:

                    return Response(
                        {"detail": "Session is in use, log out first"},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED,
                    )
                else:
                    Response({"msg":"not authourized"}, status=status.HTTP_401_UNAUTHORIZED)
            
            user = ser.instance

            request.user = user

            if user.is_superuser:

                print(user)

                django_login(request._request, user)

                return Response("")
            else:
               return Response({"msg":"not authourized"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(ser.errors, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        """
        Destroy the session.

        for anonymous users that means having their basket destroyed as well,
        because there is no way to reach it otherwise.
        """
        request = request._request
        if request.user.is_anonymous:
            pass

        request.session.clear()
        request.session.delete()
        request.session = None

        return Response("")


class UserDetail(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
        #return Response(status=status.HTTP_204_NO_CONTENT)


class RegistrationView(APIView, RegisterUserMixin):
    """
    API for registering users

    POST(email, password1, password2):
    {
        "email": "user@my-domain.com",
        "password1": "MyVerySecretPassword123"
        "password2": "MyVerySecretPassword123"
    }

    Will create a new user when the user with the specific email does
    not exist (HTTP_201_CREATED). It will also send a user_registered signal.

    It won't login the newly created user, You can do this with the login API.
    """

    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        if not getattr(settings, "OSCARAPI_ENABLE_REGISTRATION", False):
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        ser = self.serializer_class(data=request.data)

        if ser.is_valid():
            # create the user
            user = ser.save()

            if getattr(settings, "OSCAR_SEND_REGISTRATION_EMAIL", False):
                self.send_registration_email(user)
            # send the same signal as oscar is sending
            user_registered.send(sender=self, request=request, user=user)

            return Response(user.email, status=status.HTTP_201_CREATED)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class OfficeLoginView(APIView):
    """
    Api for logging in users.

    DELETE:
    Log the user out by destroying the session.
    Anonymous users will have their cart destroyed as well, because there is
    no way to reach it anymore

    POST(username, password):
    1. The user will be authenticated. The next steps will only be
       performed is login is successful. Logging in logged in users results in
       405.

    GET:

    """

    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if getattr(settings, "OSCARAPI_EXPOSE_USER_DETAILS", False):
                ser = UserSerializer(request.user, many=False)
                return Response(ser.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise MethodNotAllowed("GET")


    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():


            user = ser.instance

            # refuse to login logged in users, to avoid attaching sessions to
            # multiple users at the same time.
            if request.user.is_authenticated and request.user.is_staff:
                return Response(
                    {"detail": "Session is in use, log out first"},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED,
                )

            request.user = user

            if user.is_staff:

                django_login(request._request, user)

                return Response("")

        return Response(ser.errors, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        """
        Destroy the session.

        for anonymous users that means having their basket destroyed as well,
        because there is no way to reach it otherwise.
        """
        request = request._request
        if request.user.is_anonymous:
            pass

        request.session.clear()
        request.session.delete()
        request.session = None

        return Response("")



class StatusQuestAPIView(APIView):
    pass


class SearchOrdersAPIView(APIView):
    pass


class SearchDrugtestAPIView(APIView):
    pass


class DrugtestAPIView(APIView):
    pass