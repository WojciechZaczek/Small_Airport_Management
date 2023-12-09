# Generated by Django 4.2.2 on 2023-10-21 10:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0026_alter_notification_date_posted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="date_posted",
            field=models.DateTimeField(
                default=django.utils.timezone.now, help_text="Date post"
            ),
        ),
    ]