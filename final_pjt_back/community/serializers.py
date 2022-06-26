from rest_framework import serializers
from .models import Review, ReviewComment
from accounts.serializers import UserSerializer


class ReviewCommentSerial(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, )

    class Meta:
        model = ReviewComment
        fields = ('id', 'content', 'user', 'created_at', )


class ReviewSerial(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, )

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'user', 'created_at', 'updated_at', )
