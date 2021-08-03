from django.urls import path
from .views import RegisterView, EmailVerify, LoginView, LogoutView, RequestPasswordResetEmail, PasswordTokenCheckAPI, PasswordChangeAPI
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('mail_verify/', EmailVerify.as_view(), name='mail_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset_email/', RequestPasswordResetEmail.as_view(), name='password_reset_email'),
    path('password_reset/<uidb64>/<token>', PasswordTokenCheckAPI.as_view(), name='password_reset'),
    path('password_change', PasswordChangeAPI.as_view(), name='password_change')
]
