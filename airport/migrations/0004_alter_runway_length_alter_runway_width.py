# Generated by Django 4.2.2 on 2023-08-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0003_alter_airport_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="runway",
            name="length",
            field=models.FloatField(help_text="Runway length in meters"),
        ),
        migrations.AlterField(
            model_name="runway",
            name="width",
            field=models.FloatField(help_text="Runway width in meters"),
        ),
    ]
