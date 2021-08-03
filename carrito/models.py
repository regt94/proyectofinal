from django.db import models
from curso.models import Curso
from authentication.models import User

# Create your models here.
class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ShoppingCart'
        verbose_name_plural = 'ShoppingCarts'
