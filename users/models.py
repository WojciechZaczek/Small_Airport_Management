from django.db import models
from django.contrib.auth.models import AbstractUser
from organization.models import Department, Company
from django.urls import reverse


class CustomUser(AbstractUser):
    department = models.CharField(
        max_length=50,
        choices=Department.DEPARTAMENT,
        help_text="Users work department, model department in organization app",
    )
    job_position = models.CharField(
        max_length=20,
        choices=Department.JOB_TITLES,
        help_text="Users work job title, model worker in organization app",
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        help_text="Company ID",
    )

    def get_absolute_url(self):
        return reverse("users_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username
