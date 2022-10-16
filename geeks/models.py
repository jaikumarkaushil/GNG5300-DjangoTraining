from audioop import reverse
from django.utils import timezone
from django.db import models
from django.shortcuts import (HttpResponseRedirect)
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length = 30, default='')
    artist = models.CharField(max_length = 30, default='')
    genre = models.CharField(max_length = 30, default='')
  
    def __str__(self):
        return self.title

class Song(models.Model):
    name = models.CharField(max_length = 100, default='')
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
  
    def __str__(self):
        return self.name
        
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title 
