# Generated by Django 3.0.5 on 2023-10-03 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("client_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=70)),
                ("brokerage", models.IntegerField()),
                (
                    "date",
                    models.DateField(blank=True, default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
