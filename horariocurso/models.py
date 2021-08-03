from django.db import models
from curso.models import Curso

# Create your models here.
class Horariocurso(models.Model):
  id = models.AutoField(primary_key=True)
  curso = models.ForeignKey(Curso, related_name='horarios', on_delete=models.CASCADE)
  frecuencia = models.CharField(max_length=255,null=False)
  horario = models.CharField(max_length=255,null=False)

  def __str__(self):
      return '{}'.format(self.curso,self.frecuencia)

  class Meta:
      verbose_name_plural = "Horariocursos"