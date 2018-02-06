from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    # /music/register/
    # path('register/', views.UserFormView.as_view(), name='register'),
    # /music/51/
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/2/
    path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete/
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    # /music/album/2/favorite/
    path('album/<pk>/favorite/', views.AlbumFavorite, name='album-favorite'),
    # /music/2/1/delete/
    path('<int:album_id>/<int:song_id>/delete/', views.SongDelete, name='song-delete'),
    # /music/2/add/
    path('<int:album_id>/add/', views.SongAdd.as_view(), name='song-add'),
    # /music/2/1/play
    path('<int:album_id>/<int:song_id>/play/', views.SongPlay, name='song-play'),

]
