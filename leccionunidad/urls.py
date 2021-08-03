from django.contrib import admin
from django.urls import path, include
from .views import LeccionunidadListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('v1/leccionesunidades', LeccionunidadViewSet, basename='leccionesunidades')

urlpatterns = [
  path('', LeccionunidadListView.as_view(), name='leccionesunidades'),
]

urlpatterns += router.urls