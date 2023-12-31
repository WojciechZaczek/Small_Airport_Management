# Generated by Django 4.2.2 on 2023-09-24 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0005_client_company_id"),
        ("airport", "0007_alter_outsideaircraftstand_size"),
        ("aircraft", "0003_remove_aircrafthangared_client_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="aircrafthangared",
            name="airport_id",
            field=models.ForeignKey(
                blank=True,
                help_text="Airport ID",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="airport.airport",
            ),
        ),
        migrations.AddField(
            model_name="aircrafthangared",
            name="client_id",
            field=models.ForeignKey(
                blank=True,
                help_text="Client ID",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.client",
            ),
        ),
    ]
