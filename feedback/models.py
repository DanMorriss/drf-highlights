from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    """Model for the feedback form"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Order the most recent feedback first"""
        ordering = ['-created_at']

    def __str__(self):
        return self.content
