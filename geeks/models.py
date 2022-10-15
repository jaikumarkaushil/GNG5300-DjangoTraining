from django.utils import timezone
from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200, default='')
    description = models.TextField(default='')
    last_modified = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title 
