from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length= 100)
    short_description = models.CharField(max_length= 50)
    description = models.TextField(max_length= 250)
    price = models.FloatField()
