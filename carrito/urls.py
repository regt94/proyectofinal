from django.contrib import admin
from django.urls import path, include
from .views import CarritoViewSet, CarritoListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CarritoViewSet, basename='carrito')

urlpatterns = [
  path('/user/', CarritoListView.as_view(), name='carrito_by_user'),
]

urlpatterns += router.urls