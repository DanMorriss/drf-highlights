from rest_framework import serializers
from .models import Highlight
from likes.models import Like


class HighlightSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value is None:
            return
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, highlight=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Highlight
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_on',
            'updated_on',
            'title',
            'description',
            'improve',
            'category',
            'image',
            'location',
            'tagged_user',
            'like_id',
            'comments_count',
            'likes_count',
        ]
