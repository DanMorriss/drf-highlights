# Generated by Django 3.2.23 on 2024-02-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0012_alter_highlight_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]