from django.db import models
from organization.models import Department


class Building(models.Model):
    name = models.CharField(max_length=50, help_text="Building name or no.")
    description = models.TextField(help_text="Description")
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )


class Vehicle(models.Model):
    type = models.CharField(max_length=50, help_text="Building name or no.")
    registration_no = models.CharField(
        max_length=50, help_text="Registration no.", null=True, blank=True
    )
    description = models.TextField(help_text="Description")
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )


class Property(models.Model):
    name = models.CharField(max_length=50, help_text="Name or no.")
    description = models.TextField(help_text="Description")
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )


class Others(models.Model):
    name = models.CharField(max_length=50, help_text="Name or no.")
    description = models.TextField(help_text="Description")
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department_id"
    )
