# Generated by Django 4.2.2 on 2023-11-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0006_alter_worker_job_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(
                choices=[
                    ("office", "Airport office"),
                    ("control", "Flight control"),
                    ("mechanic", "Aircraft machinery"),
                    ("cleaning", "Aircraft cleaning department"),
                    ("air", "Aircraft Crew"),
                    ("IT", "IT department"),
                    ("external", "External Company"),
                ],
                help_text="Name of department",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="department",
            field=models.CharField(
                choices=[
                    ("office", "Airport office"),
                    ("control", "Flight control"),
                    ("mechanic", "Aircraft machinery"),
                    ("cleaning", "Aircraft cleaning department"),
                    ("air", "Aircraft Crew"),
                    ("IT", "IT department"),
                    ("external", "External Company"),
                ],
                help_text=" Worker department, model department in organization app",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="job_position",
            field=models.CharField(
                choices=[
                    ("ceo", "CEO"),
                    ("manager", "Manager"),
                    ("worker", "Worker"),
                    ("specialist", "Specialist"),
                    ("pilot", "Aircraft pilot"),
                    ("none", "None"),
                    ("admin", "Administrator IT"),
                ],
                help_text="Worker  job title, model worker in organization app",
                max_length=20,
            ),
        ),
    ]
