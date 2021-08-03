from django.contrib import admin
from django.urls import path, include
from .views import InteresadoViewSet, InteresadoCreateAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', InteresadoViewSet, basename='interesados')

urlpatterns = [
  path('create/', InteresadoCreateAPI.as_view(), name='create'),
]

urlpatterns += router.urls