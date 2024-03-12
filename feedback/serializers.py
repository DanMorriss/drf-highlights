from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        """Meta field to specify the model and fields"""
        model = Feedback
        fields = [
            'id',
            'user',
            'content',
            'created_at'
        ]
