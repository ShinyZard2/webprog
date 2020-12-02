from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    buy_now = models.CharField(max_length=100)
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title
