from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.


class News(models.Model):

    name = models.CharField(max_length=500)
    headline = models.TextField()  # short_text in place of title in course
    body_text = models.TextField()
    date = models.DateField(default=timezone.now)
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50, default="-")
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    def __str__(self):
        return self.name