# Generated by Django 4.2.2 on 2023-09-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0006_airport_company_id"),
        ("offer", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="airport_id",
            field=models.ForeignKey(
                default=1,
                help_text="Airport ID",
                on_delete=django.db.models.deletion.CASCADE,
                to="airport.airport",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="training",
            name="airport_id",
            field=models.ForeignKey(
                default=1,
                help_text="Airport ID",
                on_delete=django.db.models.deletion.CASCADE,
                to="airport.airport",
            ),
            preserve_default=False,
        ),
    ]
