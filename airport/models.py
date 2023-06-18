from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    type = models.TextField(max_length=30)
    description = models.TextField(max_length=300)
