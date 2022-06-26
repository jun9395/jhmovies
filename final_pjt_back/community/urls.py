from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_index),
    path('create/', views.create_review),
    path('update-delete/', views.update_delete_review),
    path('comment/', views.list_review_comment),
    path('comment/create/', views.create_review_comment),
    path('comment/delete/', views.delete_review_comment),
]
