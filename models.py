from django.db import models

# Create your models here.

class Input_Url(models.Model):
    names = models.CharField(max_length = 200)
