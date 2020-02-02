from django.db import models
from Accounts.models import *


class Category(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Basket(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    baskets = models.ForeignKey(Basket, on_delete=models.PROTECT, related_name='products')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
