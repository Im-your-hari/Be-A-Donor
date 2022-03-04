from django.db import models

# Create your models here.
class Search(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    district = models.CharField(max_length=50)
    blood = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

class Join(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    district = models.CharField(max_length=50)
    blood = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
