from django.db import models
from curso.models import Curso

# Create your models here.
class Unidadcurso(models.Model):
  id = models.AutoField(primary_key=True)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  desc_corta = models.CharField(max_length=100)
  desc_larga = models.CharField(max_length=255)

  def __str__(self):
    #   return '{}'.format(self.curso) + self.desc_corta
      return str(self.curso) + ' - ' +str(self.desc_corta)

  class Meta:
      verbose_name_plural = "Unidadcursos"