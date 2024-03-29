# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from location.models import Location
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Highlight(models.Model):
    """
    A class for the highlight model
    """
    categories = [
        ('family-and-friends', 'Family and Friends'),
        ('pets-and-animals', 'Pets and Animals'),
        ('relationships', 'Relationships'),
        ('health-and-fitness', 'Health and Fitness'),
        ('food-and-drink', 'Food and Drink'),
        ('self-care', 'Self-Care'),
        ('creativity', 'Creativity'),
        ('entertainment-and-music', 'Entertainment and Music'),
        ('travel-and-adventure', 'Travel and Adventure'),
        ('work-and-education', 'Work and Education'),
        ('funny', 'Funny'),
        ('other', 'Other'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    improve = models.TextField(blank=True)
    category = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default=None,
        choices=categories
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    tagged_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='tagged_user',
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
