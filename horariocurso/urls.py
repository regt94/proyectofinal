from django.contrib import admin
from django.urls import path, include
from .views import HorariocursoListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
  path('', HorariocursoListView.as_view(), name='horarioscursos'),
]

urlpatterns += router.urls