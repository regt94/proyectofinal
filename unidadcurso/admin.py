from django.contrib import admin

from .models import Unidadcurso 
# Register your models here.

@admin.register(Unidadcurso)
class UnidadcursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'desc_corta', 'desc_larga']
