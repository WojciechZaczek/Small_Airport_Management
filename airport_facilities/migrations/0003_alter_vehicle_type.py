# Generated by Django 4.2.2 on 2024-01-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "airport_facilities",
            "0002_rename_department_id_building_department_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="type",
            field=models.CharField(help_text="Vehicle type", max_length=50),
        ),
    ]