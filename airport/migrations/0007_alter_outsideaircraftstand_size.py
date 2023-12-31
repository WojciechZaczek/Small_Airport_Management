# Generated by Django 4.2.2 on 2023-09-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0006_airport_company_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outsideaircraftstand",
            name="size",
            field=models.CharField(
                choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
                help_text="Stand size. From tuple AIRCRAFT_STAND_SIZE",
                max_length=100,
            ),
        ),
    ]
