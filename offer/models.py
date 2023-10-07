from django.db import models
from users.models import Worker
from airport.models import Airport


class Offer(models.Model):
    name = models.CharField(max_length=50, help_text="Name of offer")
    price = models.FloatField(help_text="Price of offer")
    description = models.TextField(help_text="Description of offer")
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )


class Training(models.Model):
    name = models.CharField(max_length=50, help_text="Name of training")
    price = models.FloatField(help_text="Price of training")
    description = models.TextField(help_text="Description of training")
    hours = models.IntegerField(help_text="Number of hours the course takes")
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, help_text="Teachers ID"
    )
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )
