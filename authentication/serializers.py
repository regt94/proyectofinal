from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'El usuario solo debe contener caracteres alfanumericos'
    }

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerifySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Credenciales erroneas, vuelva a intentar')

        if not user.is_active:
            raise AuthenticationFailed('Su cuenta no esta activa, comuniquese con el administrador')

        if not user.is_verified:
            raise AuthenticationFailed('Su correo no esta verificado')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': 'Token expirado o incorrecto'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token') # raise


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=3)
    redirect_url = serializers.CharField(max_length=255, required=False)
    
    class Meta:
        fields = ['email']


class PasswordTokenCheckSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['token', 'uidb64']

class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=60, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']
        
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('El token no es correcto')

            user.set_password(password)
            user.save()
            return {
                'user': user
            }
        except DjangoUnicodeDecodeError as error:
            raise AuthenticationFailed('El token es incorrecto')
        except Exception as error:
            raise AuthenticationFailed('El token es incorrecto')
