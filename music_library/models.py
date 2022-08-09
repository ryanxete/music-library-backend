from django.db import models

# Create your models here.
class music(models.Model):
    artist = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    release_date = models.IntegerField()
    album = models.CharField(max_length=100)
