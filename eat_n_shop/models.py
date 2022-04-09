from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    nowHave = models.IntegerField
    eaten = models.IntegerField
    unitMeasure = models.CharField(max_length=100)
    min = models.IntegerField
    purchased = models.BooleanField(default=False)
    imageURL = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
