from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Highlight
from .serializers import HighlightSerializer
from drf_highlights.permissions import IsOwnerOrReadOnly


class HighlightList(generics.ListCreateAPIView):
    queryset = Highlight.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('like', distinct=True)
    ).order_by('-created_on')
    serializer_class = HighlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
        'tagged_user__username',
        'description',
        # 'location',
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HighlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Highlight.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('like', distinct=True)
    ).order_by('-created_on')
    serializer_class = HighlightSerializer
    permission_classes = [IsOwnerOrReadOnly]
