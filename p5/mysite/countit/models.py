

from django.db import models
from django.utils import timezone


class PersonalInformation(models.Model):
    height = models.FloatField(null=True)
    age = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    name = models.CharField(null=True,max_length=200)
    gender = models.CharField(null=True,max_length=128)
    calories = models.FloatField(null=True)
   

    def __str__(self):
        return self.name 