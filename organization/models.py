from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, help_text="Name of Company")
    address = models.TextField(
        max_length=200, help_text="Companies head office address"
    )
    telephone = models.TextField(max_length=100, help_text="Companies contact phone no")
    email_domain = models.TextField(max_length=50, help_text="Companies email_domina")
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Other important information about Company",
    )

    def __str__(self):
        return self.name


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
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, help_text="Company ID"
    )

    def __str__(self):
        return self.name


class Worker(models.Model):
    first_name = models.CharField(max_length=50, help_text="Name of worker")
    last_name = models.CharField(max_length=50, help_text="Name of worker")
    department = models.CharField(
        max_length=50,
        choices=Department.DEPARTAMENT,
        help_text=" Worker department, model department in organization app",
    )
    job_position = models.CharField(
        max_length=20,
        choices=Department.JOB_TITLES,
        help_text="Worker  job title, model worker in organization app",
    )

    address = models.CharField(max_length=100, help_text="Worker address")

    phone_no = models.CharField(max_length=50, help_text="Worker phone no.")

    information = models.TextField(max_length=50, help_text="Information about worker")

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, help_text="Company ID"
    )

    def get_absolute_url(self):
        return reverse("workers_details", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
