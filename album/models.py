from django.db import models
from musician.models import Musician
# Create your models here.


class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_name = models.CharField(max_length=100)
    rating =models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)])

    def __str__(self):
        return self.album_name

