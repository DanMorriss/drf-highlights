# Generated by Django 3.2.23 on 2024-02-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0011_alter_highlight_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='category',
            field=models.CharField(blank=True, choices=[('family-and-friends', 'Family and Friends'), ('pets-and-animals', 'Pets and Animals'), ('relationships', 'Relationships'), ('health-and-fitness', 'Health and Fitness'), ('food-and-drink', 'Food and Drink'), ('self-care', 'Self-Care'), ('creativity', 'Creativity'), ('entertainment-and-music', 'Entertainment and Music'), ('travel-and-adventure', 'Travel and Adventure'), ('work-and-education', 'Work and Education'), ('funny', 'Funny'), ('other', 'Other')], default=None, max_length=250, null=True),
        ),
    ]