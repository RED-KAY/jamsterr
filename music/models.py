from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.FileField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250, default='')
    link = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.id})

    def __str__(self):
        return self.title


class FavoriteAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' likes ' + self.album.title

