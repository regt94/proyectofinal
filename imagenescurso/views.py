from django.shortcuts import render
from .models import Imagenescurso
from .serializers import ImagenescursoSerializer
# from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters


# Create your views here.


# class ImagenescursoViewSet(viewsets.ModelViewSet):
#     queryset = Imagenescurso.objects.all()
#     serializer_class = ImagenescursoSerializer
#     # permission_classes = (permissions.IsAuthenticated, )

class ImagenescursoListView(generics.ListAPIView):
    queryset = Imagenescurso.objects.all()
    serializer_class = ImagenescursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['curso__id']