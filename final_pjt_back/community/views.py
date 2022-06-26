from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Review, ReviewComment
from .serializers import ReviewSerial, ReviewCommentSerial
from movies.models import Movie

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def review_index(request):
    movie = get_object_or_404(Movie, pk=request.data['movie']['id'])
    reviews = movie.moviereviews.order_by('-id')
    reviewserial = ReviewSerial(reviews, many=True)
    return Response(reviewserial.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request):
    movie = get_object_or_404(Movie, pk=request.data['movie']['id'])
    reviewserial = ReviewSerial(data={
        'title': request.data['title'], 'content': request.data['content'],
    })

    if reviewserial.is_valid(raise_exception=True):
        reviewserial.save(user=request.user, movie=movie)
        return Response(reviewserial.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_delete_review(request):
    review = get_object_or_404(Review, pk=request.data['review']['id'])
    movie_id = request.data['movie']['id']

    if not review.user == request.user:
        return Response({ '작성오류': '권한이 없습니다' })
    
    if request.method == 'PUT':
        reviewserial = ReviewSerial(review, data={'title': request.data['title'], 'content': request.data['content']})
        if reviewserial.is_valid(raise_exception=True):
            reviewserial.save()
            return Response(reviewserial.data)
    else:
        reviewid = review.id
        review.delete()
        return Response({ 'id': reviewid })


@api_view(['POST'])
def list_review_comment(request):
    review = get_object_or_404(Review, pk=request.data['review']['id'])
    reviewcommentserial = ReviewCommentSerial(review.reviewcomments, many=True)
    return Response(reviewcommentserial.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review_comment(request):
    review = get_object_or_404(Review, pk=request.data['review']['id'])
    reviewcommentserial = ReviewCommentSerial(data={'content': request.data['content'],})
    if reviewcommentserial.is_valid(raise_exception=True):
        reviewcommentserial.save(user=request.user, review=review)
        return Response(reviewcommentserial.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_review_comment(request):
    reviewcomment = get_object_or_404(ReviewComment, pk=request.data['commentId'])
    
    if not reviewcomment.user == request.user:
        return Response({ '작성오류': '권한이 없습니다' })
    
    reviewcomment.delete()
    return Response({ 'id': request.data['commentId']})
