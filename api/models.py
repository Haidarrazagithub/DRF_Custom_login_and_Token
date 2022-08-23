from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    city=models.CharField(max_length=50)