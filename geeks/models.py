from unittest.util import _MAX_LENGTH
from django.db import models

GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    geeks_field = models.CharField(max_length = 10, choices = GEEKS_CHOICES)
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")  # need to install Pillow for using ImageField

    def __str__(self):
        return self.title 
