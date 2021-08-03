from django.shortcuts import render
from .models import Horariocurso
from .serializers import HorariocursoSerializer
# from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters


# Create your views here.


# class HorariocursoViewSet(viewsets.ModelViewSet):
#     queryset = Horariocurso.objects.all()
#     serializer_class = HorariocursoSerializer
#     # permission_classes = (permissions.IsAuthenticated, )

class HorariocursoListView(generics.ListAPIView):
    queryset = Horariocurso.objects.all()
    serializer_class = HorariocursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['curso__id']