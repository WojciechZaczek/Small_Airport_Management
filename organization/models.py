from django.db import models


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
    company_id = models.ForeignKey(
        Company, on_delete=models.CASCADE, help_text="Airport ID"
    )
