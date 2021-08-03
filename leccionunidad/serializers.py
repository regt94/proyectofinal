from rest_framework import serializers
from .models import Leccionunidad
# from unidadcurso.serializers import UnidadcursoSerializer

class LeccionunidadSerializer(serializers.ModelSerializer):
    # unidad = UnidadcursoSerializer()
    class Meta:
        model= Leccionunidad
        fields = '__all__'
