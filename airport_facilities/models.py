from django.db import models
from organization.models import Department
from airport.models import Airport
from django.urls import reverse


class Building(models.Model):
    name = models.CharField(max_length=50, help_text="Building name or no.")
    description = models.TextField(help_text="Description")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Aiport ID", null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("buildings_details", kwargs={"pk": self.pk})


class Vehicle(models.Model):
    type = models.CharField(max_length=50, help_text="Building name or no.")
    registration_no = models.CharField(
        max_length=50, help_text="Registration no.", null=True, blank=True
    )
    description = models.TextField(help_text="Description")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Aiport ID", null=True, blank=True
    )


class Property(models.Model):
    name = models.CharField(max_length=50, help_text="Name or no.")
    description = models.TextField(help_text="Description")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Aiport ID", null=True, blank=True
    )


class Others(models.Model):
    name = models.CharField(max_length=50, help_text="Name or no.")
    description = models.TextField(help_text="Description")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )
    airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Aiport ID", null=True, blank=True
    )
