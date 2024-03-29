# Generated by Django 4.2.2 on 2024-02-19 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("airport", "0001_initial"),
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Training",
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
                ("name", models.CharField(help_text="Name of training", max_length=50)),
                ("price", models.FloatField(help_text="Price of training")),
                ("description", models.TextField(help_text="Description of training")),
                (
                    "hours",
                    models.IntegerField(help_text="Number of hours the course takes"),
                ),
                (
                    "airport",
                    models.ForeignKey(
                        help_text="Airport ID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="airport.airport",
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        help_text="Teachers ID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.worker",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
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
                ("name", models.CharField(help_text="Name of offer", max_length=50)),
                ("price", models.FloatField(help_text="Price of offer")),
                ("description", models.TextField(help_text="Description of offer")),
                (
                    "airport",
                    models.ForeignKey(
                        help_text="Airport ID",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="airport.airport",
                    ),
                ),
            ],
        ),
    ]
