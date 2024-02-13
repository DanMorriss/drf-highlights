from django.db import models
from django.contrib.auth.models import User


class Highlight(models.Model):
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
    category = models.CharField(
        max_length=250,
        choices=categories,
        default='family-and-friends'
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_image_rfyixk',
        blank=True
    )
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    tagged_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tagged_user'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
