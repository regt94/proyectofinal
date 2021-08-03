from django.db import models
from authentication.models import User
from curso.models import Curso

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails'