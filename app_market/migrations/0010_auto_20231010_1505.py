# Generated by Django 3.0.5 on 2023-10-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0009_auto_20231010_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
