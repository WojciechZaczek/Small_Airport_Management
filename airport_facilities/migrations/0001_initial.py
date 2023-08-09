# Generated by Django 4.2.2 on 2023-08-07 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
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
                    "type",
                    models.CharField(help_text="Building name or no.", max_length=50),
                ),
                (
                    "registration_no",
                    models.CharField(
                        blank=True,
                        help_text="Registration no.",
                        max_length=50,
                        null=True,
                    ),
                ),
                ("description", models.TextField(help_text="Description")),
                (
                    "department_id",
                    models.ForeignKey(
                        help_text="Department_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
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
                ("name", models.CharField(help_text="Name or no.", max_length=50)),
                ("description", models.TextField(help_text="Description")),
                (
                    "department_id",
                    models.ForeignKey(
                        help_text="Department_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Others",
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
                ("name", models.CharField(help_text="Name or no.", max_length=50)),
                ("description", models.TextField(help_text="Description")),
                (
                    "department_id",
                    models.ForeignKey(
                        help_text="Department_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Building",
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
                    models.CharField(help_text="Building name or no.", max_length=50),
                ),
                ("description", models.TextField(help_text="Description")),
                (
                    "department_id",
                    models.ForeignKey(
                        help_text="Department_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.department",
                    ),
                ),
            ],
        ),
    ]