from django.db import models
from django.contrib.auth.models import User
from highlights.models import Highlight


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content
