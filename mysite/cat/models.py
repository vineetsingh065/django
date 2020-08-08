from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.


class Cat(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name