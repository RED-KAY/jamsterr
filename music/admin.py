from django.contrib import admin
from .models import Album, Song, FavoriteAlbum

# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(FavoriteAlbum)
