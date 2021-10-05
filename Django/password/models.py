from django.db import models

# Create your models here.

class Users(models.Model):
    user = models.EmailField()
    password = models.CharField(max_length=30)
    data = models.DateField()