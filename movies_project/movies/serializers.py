from rest_framework import serializers
from .models import Movie, StreamingChannel

__all__ = ["MovieSerializer", "StreamingChannelSerializer"]


class StreamingChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamingChannel
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = [
            'id', 'owner', 'title', 'subtitle', 'director',
            'description', 'channels'
        ]
