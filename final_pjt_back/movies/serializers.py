from .models import Movie, Genre, MovieComment
from community.serializers import ReviewSerial
from accounts.serializers import UserSerializer

from rest_framework import serializers


class GenreSerial(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieCommentSerial(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, )

    class Meta:
        model = MovieComment
        fields = ('id', 'content', 'score', 'user', )


class MovieSerial(serializers.ModelSerializer):
    genres = GenreSerial(many=True, read_only=True, )
    moviereviews = ReviewSerial(many=True, read_only=True, )
    moviecomments = MovieCommentSerial(many=True, read_only=True, )

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'vote_average', 'popularity', 'overview', 'poster_path', 'genres', 'moviereviews', 'moviecomments', )