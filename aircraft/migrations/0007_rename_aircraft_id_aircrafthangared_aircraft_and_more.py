# Generated by Django 4.2.2 on 2023-10-30 16:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aircraft", "0006_aircrafthangared_airport_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="aircrafthangared",
            old_name="aircraft_id",
            new_name="aircraft",
        ),
        migrations.RenameField(
            model_name="aircrafthangared",
            old_name="airport_id",
            new_name="airport",
        ),
        migrations.RenameField(
            model_name="aircrafthangared",
            old_name="client_id",
            new_name="client",
        ),
        migrations.RenameField(
            model_name="aircrafthangared",
            old_name="hangar_id",
            new_name="hangar",
        ),
        migrations.RenameField(
            model_name="aircrafthangared",
            old_name="outside_stand_id",
            new_name="outside_stand",
        ),
    ]
