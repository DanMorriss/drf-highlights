from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from drf_highlights.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    # annotate adds a new field to the queryset
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__highlight', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'location',
        'name',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__highlight', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
