from django.db import models

# Create your models here.
class TixGet(models.Model):
    managed = False
    start = models.DateField()
    end = models.DateField()
    genre = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15)
