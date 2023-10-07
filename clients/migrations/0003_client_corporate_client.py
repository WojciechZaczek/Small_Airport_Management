# Generated by Django 4.2.2 on 2023-09-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="corporate_client",
            field=models.BooleanField(
                default=1, help_text="If client is a corporate - Yes/No"
            ),
            preserve_default=False,
        ),
    ]
