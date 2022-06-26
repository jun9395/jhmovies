import requests
from decouple import config
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Genre, MovieComment
from community.models import Review
from .serializers import MovieSerial, GenreSerial, MovieCommentSerial


API_KEY = config('API_KEY')

@api_view(['GET'])
def index(request):
    if not Genre.objects.all():
        url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-kr'
        genres = requests.get(url).json()['genres']
        for genre in genres:
            n_genre = Genre()
            n_genre.id = genre['id']
            n_genre.name = genre['name']
            n_genre.save()

    if not Movie.objects.all():
        PAGE = 15    # 한 페이지에 20개
        for i in range(1, PAGE + 1):
            url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={i}'
            # https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-KR&page={i}
            popularmovie = requests.get(url).json().get('results')
            for movie in popularmovie:
                n_movie = Movie()
                n_movie.title = movie['title']
                n_movie.release_date = movie['release_date']
                n_movie.vote_average = movie['vote_average']
                n_movie.popularity = int(movie['popularity'] * 10000)
                n_movie.overview = movie['overview']
                n_movie.poster_path = 'https://image.tmdb.org/t/p/w500' + movie['poster_path']
                n_movie.save()
                for genre_id in movie['genre_ids']:
                    n_movie.genres.add(Genre.objects.get(id=genre_id))

    movies = Movie.objects.order_by('-vote_average')
    movieserial = MovieSerial(movies, many=True)
    return Response(movieserial.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
    genres = Genre.objects.all()
    genreserial = GenreSerial(genres, many=True)
    comments = MovieComment.objects.all()
    reviews = Review.objects.all()

    watchedmovies = []
    for comment in comments:
        if comment.user == request.user:
            watchedmovies.append(comment.movie.id)
    for review in reviews:
        if review.user == request.user:
            watchedmovies.append(review.movie.id)
    watchedmovies = list(set(watchedmovies))

    return Response({'genres': genreserial.data, 'watchedmovies': watchedmovies})


@api_view(['POST'])
def list_movie_comment(request):
    movie = get_object_or_404(Movie, pk=request.data['movie']['id'])
    moviecommentserial = MovieCommentSerial(movie.moviecomments, many=True)
    return Response(moviecommentserial.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_movie_comment(request):
    movie = get_object_or_404(Movie, pk=request.data['movie']['id'])
    moviecommentserial = MovieCommentSerial(data={
        'content': request.data['content'],
        'score': request.data['rating']
    })
    
    if moviecommentserial.is_valid(raise_exception=True):
        moviecommentserial.save(user=request.user, movie=movie)
        return Response(moviecommentserial.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_delete_movie_comment(request):
    movie = get_object_or_404(Movie, pk=request.data['movie']['id'])
    moviecomment = get_object_or_404(MovieComment, pk=request.data['commentId'])

    if not moviecomment.user == request.user:
        return Response({ '작성오류': '권한이 없습니다' })

    if request.method == 'PUT':
        moviecommentserial = MovieCommentSerial(moviecomment, data={'content': request.data['content'], 'score': request.data['rating']})
        if moviecommentserial.is_valid(raise_exception=True):
            moviecommentserial.save()
            return Response(moviecommentserial.data)
    else:
        moviecomment.delete()
        return Response({ 'id': request.data['commentId']})
