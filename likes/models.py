from django.db import models
from django.contrib.auth.models import User
from highlights.models import Highlight


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'highlight']

    def __str__(self):
        return f'{self.owner} {self.highlight}'
