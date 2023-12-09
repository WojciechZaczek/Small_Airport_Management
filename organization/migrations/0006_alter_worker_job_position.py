# Generated by Django 4.2.2 on 2023-11-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0005_rename_company_id_department_company"),
    ]

    operations = [
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
                ],
                help_text="Worker  job title, model worker in organization app",
                max_length=20,
            ),
        ),
    ]
