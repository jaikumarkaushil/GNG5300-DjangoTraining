from django.utils import timezone
from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title 
