# Generated by Django 3.2.23 on 2024-03-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='feedback',
            name='fname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='lname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]