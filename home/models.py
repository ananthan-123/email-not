from django.db import models
from django.db.models.expressions import F
# from datetime import datetime
from django.utils import timezone


# Create your models here.


class dataModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    date = models.DateTimeField()
    activated = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='images/')

class activateModel(models.Model):
    data = models.ForeignKey(dataModel,on_delete=models.CASCADE)
    # ide = models.CharField(max_length=255)
