from django.contrib import admin

from .models import Interesado 
# Register your models here.

@admin.register(Interesado)
class InteresadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'curso', 'email', 'celular']

