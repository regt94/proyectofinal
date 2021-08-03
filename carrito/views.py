from django.shortcuts import render
from .models import ShoppingCart
from .serializers import CarritoSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters

# Create your views here.


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = CarritoSerializer
    # permission_classes = (permissions.IsAuthenticated, )


class CarritoListView(generics.ListAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = CarritoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__id']