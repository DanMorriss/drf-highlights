from rest_framework import generics, permissions
from .models import Highlight
from .serializers import HighlightSerializer
from drf_highlights.permissions import IsOwnerOrReadOnly


class HighlightList(generics.ListCreateAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HighlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [IsOwnerOrReadOnly]
