import os
from django.shortcuts import render
from rest_framework import generics, views, permissions
from .serializers import RegisterSerializer, EmailVerifySerializer, LoginSerializer, LogoutSerializer, ResetPasswordSerializer, PasswordTokenCheckSerializer, PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse_lazy, reverse
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from jwt import decode, ExpiredSignatureError, DecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError

from .helpers import send_email

from .models import User

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        # Enviar Correo
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        relative_link = reverse_lazy('mail_verify')
        url = f'http://127.0.0.1:8000{relative_link}?token={token}'

        data = {
            'subject': 'Prueba',
            'body': f'Hola {user.username}, usa este link para confirmar tu cuenta {url}',
            'to': f'{user.email}'
        }

        send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class EmailVerify(generics.GenericAPIView):
    serializer_class = EmailVerifySerializer

    token_param_config = Parameter('token', in_=IN_QUERY, description='Token', type=TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = decode(token, os.environ.get('SECRET_KEY'), algorithms='HS256')

            user = User.objects.get(id=payload['user_id'])
            message = 'El usuario ya ha sido activado anteriormente'
            if not user.is_verified:
                message = 'El usuario ha sido activado'
                user.is_verified = True
                user.save()

            return Response({
                'success': message
            }, status=status.HTTP_200_OK)

        except ExpiredSignatureError:
            return Response({
                'error': 'El token ha expirado'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except DecodeError:
            return Response({
                'error': 'Token incorrecto'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            relative_link = reverse('password_reset', kwargs={'uidb64': uidb64, 'token': token})
            url = f'http://127.0.0.1:8000{relative_link}'

            data = {
                'subject': 'Resetear contraseña',
                'body': f'Hola {user.username}, usa este link para resetear tu contraseña {url}',
                'to': f'{user.email}'
            }

            send_email(data)

        return Response({
            'success': 'El correo fue enviado'
        }, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = PasswordTokenCheckSerializer

    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise Exception('El token no es correcto')

            return Response({
                'success': 'Token correcto'
            }, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as error:
            return Response({
                'error': 'El token es incorrecto'
            }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as error:
            return Response({
                'error': 'El token es incorrecto'
            }, status=status.HTTP_401_UNAUTHORIZED)


class PasswordChangeAPI(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_200_OK)
