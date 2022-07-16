from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name