# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Highlight
from .serializers import HighlightSerializer
from drf_highlights.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class HighlightList(generics.ListCreateAPIView):
    """
    A class for the highlight list to view all highlights
    """
    queryset = Highlight.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('like', distinct=True)
    ).order_by('-created_on')
    serializer_class = HighlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'like__owner__profile',
        'owner__profile',
        'category',
        'tagged_user__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
        'tagged_user__username',
        'description',
        'improve',
        'created_on',
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        """
        Sets the owner of the highlight to the logged in user
        """
        serializer.save(owner=self.request.user)


class HighlightDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for the highlight detail for a user to
    view, update or delete a highlight
    """
    queryset = Highlight.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('like', distinct=True)
    ).order_by('-created_on')
    serializer_class = HighlightSerializer
    permission_classes = [IsOwnerOrReadOnly]
