from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, exceptions, status 
from rest_framework.response import Response
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from allauth.account.models import EmailAddress, EmailConfirmation
from rest_auth.app_settings import create_token
from rest_auth.utils import jwt_encode
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from .tasks import send_welcome_mail



sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2')
)



class RegisterAPIView(RegisterView):

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)


    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)
        email_address = EmailAddress.objects.get(user=user, email=user.email)
        email_address.verified, email_address.primary = True, True
        email_address.save()
        send_welcome_mail.delay(user.username, user.email)
        return user

class LoginAPIView(LoginView):

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()
