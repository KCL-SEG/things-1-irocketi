from django.db import models


# Create your models here.
class Thing (models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    description = models.CharField(max_length=120, blank=True)