# Generated by Django 4.2.2 on 2023-09-24 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0018_alter_notification_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 9, 24, 15, 52, 47, 262323, tzinfo=datetime.timezone.utc
                ),
                help_text="Date post",
            ),
        ),
    ]
