# Generated by Django 4.2.2 on 2023-08-20 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0003_alter_notification_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 8, 20, 9, 55, 45, 68659, tzinfo=datetime.timezone.utc
                ),
                help_text="Date post",
            ),
        ),
    ]
