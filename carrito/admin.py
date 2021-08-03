from django.contrib import admin
from .models import ShoppingCart
# Register your models here.

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'curso', 'quantity','price','user']