from django.db import models
from datetime import date

# Create your models here.
class Curso(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=200, null=False)
  titulo_largo = models.CharField(max_length=255)
  descripcion = models.CharField(max_length=255)
  estado = models.IntegerField(default=1)
  fecha_inicio = models.DateField(default=date.today)
  precio = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
      return '{}'.format(self.titulo)

  class Meta:
      verbose_name_plural = "Cursos"