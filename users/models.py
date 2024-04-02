from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from organization.models import Department, Company
from django.urls import reverse
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if not extra_fields.get("company"):
            company_name = "Admin IT"
            company, _ = Company.objects.get_or_create(
                name=company_name,
                defaults={
                    "name": company_name,
                    "address": "Default address",
                    "telephone": "123--456-789",
                    "email_domain": "admin.com",
                    "description": "default description",
                },
            )

            extra_fields["company"] = company

        return super().create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    department = models.CharField(
        max_length=50,
        choices=Department.DEPARTAMENT,
        help_text="Users work department, model department in organization app",
    )
    job_position = models.CharField(
        max_length=20,
        choices=Department.JOB_TITLES,
        default="none",
        help_text="Users work job title, model worker in organization app",
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        help_text="Company ID",
    )

    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("users_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username
