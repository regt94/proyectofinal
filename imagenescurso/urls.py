from django.contrib import admin
from django.urls import path, include
from .views import ImagenescursoListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('v1/imagenescursos', ImagenescursoViewSet, basename='imagenescursos')

urlpatterns = [
  path('', ImagenescursoListView.as_view(), name='imagenescursos'),
]

urlpatterns += router.urls