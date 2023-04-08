# Generated by Django 4.1.7 on 2023-04-08 05:41

from django.db import migrations, models
import django.db.models.deletion
import openticket.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("venues", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.FloatField()),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="venues.event"
                    ),
                ),
                (
                    "seat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="venues.seat"
                    ),
                ),
            ],
            bases=(openticket.utils.TrackedMixin, models.Model),
        ),
    ]