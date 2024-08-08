from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artist/new/', views.artist_create, name='artist_create'),
    path('artist/<int:pk>/edit/', views.artist_update, name='artist_update'),
    path('artist/<int:pk>/delete/', views.artist_delete, name='artist_delete'),

    path('albums/', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/new/', views.album_create, name='album_create'),
    path('album/<int:pk>/edit/', views.album_update, name='album_update'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
]
