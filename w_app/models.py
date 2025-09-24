from django.db import models


# Create your models here.
class History(models.Model):
    temperature=models.CharField(max_length=10)
    dew_point=models.CharField(max_length=10)
    humidity=models.CharField(max_length=10)
    wind_speed=models.CharField(max_length=10)
    visibility=models.CharField(max_length=10)
    pressure=models.CharField(max_length=10)
    res=models.CharField(max_length=100)