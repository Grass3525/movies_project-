from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .models import Movie, StreamingChannel
from .permissions import IsOwnerOrReadOnly, IsAdminOrManagerOrReadOnly
from .serializers import MovieSerializer, StreamingChannelSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StreamingChannelViewSet(viewsets.ModelViewSet):
    queryset = StreamingChannel.objects.all()
    serializer_class = StreamingChannelSerializer
    permission_classes = (IsAuthenticated, IsAdminOrManagerOrReadOnly)
