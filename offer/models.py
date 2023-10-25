from django.db import models
from django.urls import reverse
from airport.models import Airport
from organization.models import Worker


class Offer(models.Model):
    name = models.CharField(max_length=50, help_text="Name of offer")
    price = models.FloatField(help_text="Price of offer")
    description = models.TextField(help_text="Description of offer")
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )

    def get_absolute_url(self):
        return reverse("offers_details", kwargs={"pk": self.pk})


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

    def get_absolute_url(self):
        return reverse("trainings_detail", kwargs={"pk": self.pk})
