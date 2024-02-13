# Generated by Django 3.2.23 on 2024-02-13 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('highlights', '0003_alter_highlight_tagged_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='tagged_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagged_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
