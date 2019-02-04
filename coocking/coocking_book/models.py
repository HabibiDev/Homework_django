from django.db import models
from django.urls import reverse

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=False, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    

    def __str__(self):
        return self.name


class Dish(models.Model):

    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient, related_name='dishes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dish_detail', kwargs={'pk': self.pk})


class Order(models.Model):

    contact = models.CharField(max_length=120, on_delete = models.CASCADE)
    order_list = models.ManyToManyField(Ingredient, related_name='orders', through='OrderList')

    def __init__(self):
        return self.contact


class OrderList(models.Model):

    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'OrderList')
    ingredients = models.ForeignKey(Ingredient)
    date_joined = models.DateField(auto_now = True)






