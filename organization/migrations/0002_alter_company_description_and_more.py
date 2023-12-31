# Generated by Django 4.2.2 on 2023-08-30 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Other important information about Company",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="company_id",
            field=models.ForeignKey(
                help_text="Company ID",
                on_delete=django.db.models.deletion.CASCADE,
                to="organization.company",
            ),
        ),
    ]
