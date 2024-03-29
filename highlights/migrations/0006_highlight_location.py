# Generated by Django 3.2.23 on 2024-02-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_remove_location_highlight'),
        ('highlights', '0005_alter_highlight_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.location'),
        ),
    ]
