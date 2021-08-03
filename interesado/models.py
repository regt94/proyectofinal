from django.db import models
from curso.models import Curso

# Create your models here.
class Interesado(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(null=False, max_length=255)
  curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
  email = models.EmailField(max_length=50, null=False, unique=True)
  celular = models.CharField(max_length=15)

  def __str__(self):
      return '{}'.format(self.nombre)

  class Meta:
      verbose_name_plural = "Interesados"