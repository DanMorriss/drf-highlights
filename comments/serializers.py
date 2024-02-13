from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'highlight',
            'created_on',
            'updated_on',
            'content'
        ]

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)


class CommentDetailSerializer(CommentSerializer):
    highlight = serializers.ReadOnlyField(source='highlight.id')
