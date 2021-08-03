from rest_framework import serializers
from .models import Horariocurso


class HorariocursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Horariocurso
        fields = '__all__'
