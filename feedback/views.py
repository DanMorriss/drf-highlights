from rest_framework import generics, permissions, filters
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackList(generics.ListCreateAPIView):
    """Allows users to submit feedback"""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['user__username', 'content']

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
