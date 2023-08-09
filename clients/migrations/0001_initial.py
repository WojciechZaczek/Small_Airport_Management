# Generated by Django 4.2.2 on 2023-08-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AeroclubMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, help_text="Name of client", max_length=20, null=True
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="Last name of client",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        help_text="Email of client",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "address",
                    models.CharField(help_text="Address of client", max_length=200),
                ),
                ("phone_no", models.IntegerField(help_text="Phone no. of client")),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, help_text="Name of client", max_length=20, null=True
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="Last name of client",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "pesel",
                    models.IntegerField(
                        blank=True,
                        help_text=" Pesel of client",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True,
                        help_text="If client is a company, name of company",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "nip",
                    models.IntegerField(
                        blank=True,
                        help_text="If client is a company, NIP of company",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        help_text="Email of client",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "address",
                    models.CharField(help_text="Address of client", max_length=200),
                ),
                ("phone_no", models.IntegerField(help_text="Phone no. of client")),
                (
                    "aeroclub_meber",
                    models.BooleanField(
                        help_text="Information if client is a Aeroclub member"
                    ),
                ),
            ],
        ),
    ]
