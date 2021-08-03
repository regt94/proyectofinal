from rest_framework import serializers
from .models import ShoppingCart

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ShoppingCart
        fields = '__all__'


