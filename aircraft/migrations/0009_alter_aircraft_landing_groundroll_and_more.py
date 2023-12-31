# Generated by Django 4.2.2 on 2023-10-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aircraft", "0008_alter_aircraft_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircraft",
            name="landing_groundroll",
            field=models.IntegerField(
                help_text="aircraft landing distance - on the ground in meters"
            ),
        ),
        migrations.AlterField(
            model_name="aircraft",
            name="take_off_ground",
            field=models.IntegerField(
                help_text="Take off first part, where aircraft is on the ground in meters"
            ),
        ),
        migrations.AlterField(
            model_name="aircraft",
            name="take_off_over_50ft_distance",
            field=models.IntegerField(
                help_text="Take off second part, from where the vehicle leaves the ground to until it reaches 50 ft in meters"
            ),
        ),
    ]
