from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=30, help_text="Name of the airport")
    address = models.TextField(max_length=200)
    contact = models.TextField(max_length=200)
    types_of_traffic_permitted = models.TextField(max_length=200)
    radio = models.FloatField()
    elevation = models.IntegerField()
    co_ordinates = models.TextField(max_length=200)
    description = models.TextField(max_length=300)
    length = models.IntegerField()
    width = models.IntegerField()
    square_meters = models.IntegerField()
