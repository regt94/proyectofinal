from django.contrib import admin
from django.urls import path, include
from .views import OrderViewSet, OrderDetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderViewSet, basename='orden')
router.register('detail/', OrderDetailViewSet, basename='ordendetail')

urlpatterns = [
  # path('v1/orden_by_user/', OrderViewSet.as_view(), name='carrito_by_user'),
  # path('v1/ordendetail_by_user/', OrderDetailListView.as_view(), name='carrito_by_user'),
]

urlpatterns += router.urls