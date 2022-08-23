from ast import alias
from unicodedata import name
from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
