from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=70)
    password=models.CharField(max_length=70)
