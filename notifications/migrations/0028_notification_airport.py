# Generated by Django 4.2.2 on 2023-10-21 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0007_alter_outsideaircraftstand_size"),
        ("notifications", "0027_alter_notification_date_posted"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="airport",
            field=models.ForeignKey(
                default=1,
                help_text="Airport ID",
                on_delete=django.db.models.deletion.CASCADE,
                to="airport.airport",
            ),
            preserve_default=False,
        ),
    ]
