from rest_framework import serializers
from .models import Imagenescurso


class ImagenescursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Imagenescurso
        fields = '__all__'
