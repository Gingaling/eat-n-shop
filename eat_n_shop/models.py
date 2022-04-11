from django.db import models
from django.db.models import Model

# Create your models here.


class Grocery(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    nowHave = models.DecimalField(max_digits=3, decimal_places=1)
    eaten = models.DecimalField(max_digits=3, decimal_places=1)
    unitMeasure = models.CharField(max_length=100)
    min = models.DecimalField(max_digits=3, decimal_places=1)
    purchased = models.BooleanField(default=False)
    imageURL = models.CharField(max_length=200)

    def __str__(self):
        return self.name
