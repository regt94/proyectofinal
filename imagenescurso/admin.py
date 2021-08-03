from django.contrib import admin

from .models import Imagenescurso 
# Register your models here.

@admin.register(Imagenescurso)
class ImagenescursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'url']
