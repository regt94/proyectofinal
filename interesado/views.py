from django.shortcuts import render
from .models import Interesado
from .serializers import InteresadoSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from authentication.helpers import send_email
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class InteresadoViewSet(viewsets.ModelViewSet):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer
    # permission_classes = (permissions.IsAuthenticated, )


# class InteresadoViewSet(viewsets.ModelViewSet):
#     queryset = Interesado.objects.all()
#     serializer_class = InteresadoSerializer
#     # permission_classes = (permissions.IsAuthenticated, )

class InteresadoCreateAPI(generics.CreateAPIView):
    serializer_class = InteresadoSerializer
    def post(self, request, *args, **kwargs):
        interesado = request.data
        serializer = self.serializer_class(data=interesado)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        interesado_data = serializer.data

        # Enviar Correo
        email=interesado_data['email']
        nombre=interesado_data['nombre']

        data = {
            'subject': f'Descuento del 10% en todas tus compras de Cursos de IDAT',
            'body': f'Hola {nombre}, tu codigo de descuento es IDAT_2021',
            'to': f'{email}'
        }

        send_email(data)
        return Response(interesado_data, status=status.HTTP_201_CREATED)