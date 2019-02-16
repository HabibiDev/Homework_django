from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Note(models.Model):
    content = models.CharField(max_length=120)


class NotesItem(models.Model):
    note = models.ForeignKey(
        Note, on_delete=models.CASCADE, related_name='note_item')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
>>>>>>> 9095da5e5be95d1ef370d086c06c6d83d0fd6fa2
