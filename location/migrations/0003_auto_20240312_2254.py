# Generated by Django 3.2.23 on 2024-03-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_remove_location_highlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]
