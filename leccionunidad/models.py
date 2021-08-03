from django.db import models
from unidadcurso.models import Unidadcurso

# Create your models here.
class Leccionunidad(models.Model):
  id = models.AutoField(primary_key=True)
  unidad = models.ForeignKey(Unidadcurso, related_name='lecciones', on_delete=models.CASCADE)
  desc_corta = models.CharField(max_length=100, null=False)
  desc_larga = models.CharField(max_length=255)

  def __str__(self):
      return '{}'.format(self.unidad,self.desc_corta)

  class Meta:
      verbose_name_plural = "Leccionunidades"