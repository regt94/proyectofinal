from django.contrib import admin
from .models import Horariocurso 
# Register your models here.

@admin.register(Horariocurso)
class HorariocursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'frecuencia','horario']
