from django.db import models
from django.urls import reverse

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=False,
                            verbose_name='Название')
    weight = models.FloatField(verbose_name='Количество в граммах', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Dish(models.Model):

    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient, related_name='dishes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coocking_book:dish_detail', kwargs={'pk': self.pk})


class IngredientInOrder(models.Model):
    name = models.CharField(max_length=120, unique=False,
                            verbose_name='Название')
    weight = models.FloatField(verbose_name='Количество в граммах', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name='order_dish', null=True)
    contact = models.CharField(max_length=120, null=True)
    ingredients = models.ManyToManyField(IngredientInOrder, related_name = 'orders')
    order_date = models.DateField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('coocking_book:order_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return 'Тел.заказчика:{0} дата заказа:{1} блюдо:{2}'.format(self.contact, self.order_date, self.dish)


