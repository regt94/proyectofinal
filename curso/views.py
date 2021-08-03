from django.shortcuts import render
from .models import Curso
from .serializers import CursoSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    # permission_classes = (permissions.IsAuthenticated, )
