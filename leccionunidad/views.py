from django.shortcuts import render
from .models import Leccionunidad
from .serializers import LeccionunidadSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters



# Create your views here.


# class LeccionunidadViewSet(viewsets.ModelViewSet):
#     queryset = Leccionunidad.objects.all()
#     serializer_class = LeccionunidadSerializer
#     # permission_classes = (permissions.IsAuthenticated, )

    
class LeccionunidadListView(generics.ListAPIView):
    queryset = Leccionunidad.objects.all()
    serializer_class = LeccionunidadSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['unidad__id']