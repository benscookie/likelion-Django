"""
Serializers for movie APIs
"""

from rest_framework import serializers

from core.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'director', 'main_character', 'duration', 'rating', 'description']
        read_only_fields = ['id']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields
