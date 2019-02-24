from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _
from notes.models import Note
from notes.models import NotesItem
from rest_framework.authtoken.models import Token
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=False,
                            verbose_name=_('Название'))
    weight = models.FloatField(
        verbose_name=_('Количество в граммах'), blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):

    title = models.CharField(max_length=120, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='dish_author')
    description = models.TextField(blank=True, null=True)
    ingredient = models.ManyToManyField(
        Ingredient, related_name='dishes')
    note = GenericRelation(NotesItem)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def notes(self):
        return Note.objects.filter(note_item__object_id=self.id,
                                   note_item__content_type=ContentType.objects.get_for_model(self.__class__))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Dish, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coocking_book:dish_detail', kwargs={'pk': self.pk})


class IngredientInOrder(models.Model):
    name = models.CharField(max_length=120, unique=False,
                            verbose_name=_('Название'))
    weight = models.FloatField(
        verbose_name=_('Количество в граммах'), blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name='order_dish', null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='order_author')
    contact = models.CharField(max_length=120, null=True)
    ingredients = models.ManyToManyField(
        IngredientInOrder, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    note = GenericRelation(NotesItem)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def notes(self):
        return Note.objects.filter(note_item__object_id=self.id,
                                   note_item__content_type=ContentType.objects.get_for_model(self.__class__))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dish)
        super(Order, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('coocking_book:order_detail', kwargs={'pk': self.pk})

    def __str__(self):
        contact = self.contact
        order_date = self.order_date
        dish = self.dish
        return _('Тел.заказчика:{contact} дата заказа:{order_date} блюдо:{dish}').format(contact=self.contact, order_date=self.order_date, dish=self.dish)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
