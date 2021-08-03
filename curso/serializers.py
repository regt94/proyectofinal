from rest_framework import serializers
from .models import Curso
from imagenescurso.serializers import ImagenescursoSerializer
from horariocurso.serializers import HorariocursoSerializer
from unidadcurso.serializers import UnidadcursoSerializer

class CursoSerializer(serializers.ModelSerializer):
    imagenes = ImagenescursoSerializer(many=True)
    horarios = HorariocursoSerializer(many=True)

    class Meta:
        model= Curso
        fields = '__all__'
