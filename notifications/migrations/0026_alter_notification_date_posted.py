# Generated by Django 4.2.2 on 2023-10-16 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0025_alter_notification_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 16, 16, 14, 21, 204307, tzinfo=datetime.timezone.utc
                ),
                help_text="Date post",
            ),
        ),
    ]
