from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    fb = models.CharField(default='-', max_length=50)
    tw = models.CharField(default='-', max_length=50)
    yt = models.CharField(default='-', max_length=50)
    contact = models.CharField(default='0', max_length=12)

    site_name = models.CharField(default='-', max_length=50)

    def __str__(self):
        return self.site_name + " | " + str(self.pk)
