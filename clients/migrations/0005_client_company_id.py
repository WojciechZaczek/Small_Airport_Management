# Generated by Django 4.2.2 on 2023-09-23 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0002_alter_company_description_and_more"),
        ("clients", "0004_alter_client_offer_alter_client_training"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="company_id",
            field=models.ForeignKey(
                default=1,
                help_text="Company ID - information which organization client is it",
                on_delete=django.db.models.deletion.CASCADE,
                to="organization.company",
            ),
            preserve_default=False,
        ),
    ]