# Generated by Django 4.2.2 on 2023-10-07 16:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("offer", "0005_alter_training_worker"),
        ("users", "0002_customuser_company_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="company_id",
            new_name="company",
        ),
        migrations.DeleteModel(
            name="Worker",
        ),
    ]