from django.db import models
from django.urls import reverse

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=False,
                            verbose_name='Название')
    weight = models.FloatField(verbose_name='Количество в граммах')

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

    contact = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, related_name='orders')
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return 'Номер заказчика:{0}, Дата заказа:{1}'.format(self.contact, self.date_joined)
