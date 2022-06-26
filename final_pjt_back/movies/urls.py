from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recommend/', views.recommend),
    path('comment/', views.list_movie_comment),
    path('comment/create/', views.create_movie_comment),
    path('comment/update-delete/', views.update_delete_movie_comment),
]
