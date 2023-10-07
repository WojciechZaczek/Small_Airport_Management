# Generated by Django 4.2.2 on 2023-08-30 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0002_alter_company_description_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="company_id",
            field=models.ForeignKey(
                default=1,
                help_text="Company ID",
                on_delete=django.db.models.deletion.CASCADE,
                to="organization.company",
            ),
            preserve_default=False,
        ),
    ]
