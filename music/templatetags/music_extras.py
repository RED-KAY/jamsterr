from django import template
from music.models import Album, FavoriteAlbum
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag
def check_if_favorite(user, album_id):
    if user.is_anonymous:
        return None
    a = Album.objects.get(pk=album_id)
    try :
        fa = user.favoritealbum_set.get(album=a)
    except (KeyError, FavoriteAlbum.DoesNotExist):
        return None
    else:
        return fa



'''@register.simple_tag
def check_if_favorite(s, title):
	return s.username + title.title
    

    '''



