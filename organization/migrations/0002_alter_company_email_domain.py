# Generated by Django 4.2.2 on 2024-03-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="email_domain",
            field=models.TextField(help_text="Companies email_domain", max_length=50),
        ),
    ]
