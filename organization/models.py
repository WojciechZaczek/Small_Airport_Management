from django.db import models
from airport.models import Airport


class Department(models.Model):
    DEPARTAMENT = [
        ("office", "Airport office"),
        ("control", "Flight control"),
        ("mechanic", "Aircraft machinery"),
        ("cleaning", "Aircraft cleaning department"),
        ("air", "aircraft Crew"),
        ("IT", "IT department"),
    ]

    JOB_TITLES = [
        ("ceo", "CEO"),
        ("manager", "Manager"),
        ("worker", "Worker"),
        ("specialist", "Specialist"),
        (
            "pilot",
            "Aircraft pilot",
        ),
    ]

    name = models.CharField(
        max_length=50, choices=DEPARTAMENT, help_text="Name of department"
    )
    description = models.TextField(
        max_length=200, help_text="information about department"
    )
    Airport_ID = models.ForeignKey(
        Airport, on_delete=models.CASCADE, help_text="Airport ID"
    )


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    telephone = models.TextField(max_length=100)
    email_domain = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
