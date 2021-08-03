from rest_framework import serializers
from .models import Unidadcurso
from leccionunidad.serializers import LeccionunidadSerializer


class UnidadcursoSerializer(serializers.ModelSerializer):
    lecciones = LeccionunidadSerializer(many=True)
    class Meta:
        model= Unidadcurso
        fields = ['id','curso', 'desc_corta', 'desc_larga', 'lecciones']
        # fields = '__all__'
