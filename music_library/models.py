from django.db import models

# Create your models here.
class Music(models.Model):
    artist = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    album = models.CharField(max_length=100)
