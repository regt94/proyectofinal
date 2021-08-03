from django.shortcuts import render
from .models import Unidadcurso
from .serializers import UnidadcursoSerializer
# from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters



# Create your views here.


# class UnidadcursoViewSet(viewsets.ModelViewSet):
#     queryset = Unidadcurso.objects.all()
#     serializer_class = UnidadcursoSerializer
#     # permission_classes = (permissions.IsAuthenticated, )



class UnidadcursoListView(generics.ListAPIView):
    queryset = Unidadcurso.objects.all()
    serializer_class = UnidadcursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['curso__id']