from django.contrib import admin

from .models import Leccionunidad 
# Register your models here.

@admin.register(Leccionunidad)
class LeccionunidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'unidad', 'desc_corta', 'desc_larga']
