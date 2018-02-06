from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.views.generic import View
from django.urls import reverse_lazy
from .models import Album, Song, FavoriteAlbum
# from .forms import UserForm
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongAdd(CreateView):
    model = Song
    fields = ['artist', 'title', 'link']

    def form_valid(self, form):
        a = self.kwargs['album_id']
        form.instance.album = Album.objects.get(pk=a)

        link = form.instance.link
        #link = link.replace('www.youtube.com', 'youtu.be')
        link = link.replace('watch?v=','embed/')
        form.instance.link = link

        return super().form_valid(form)


def SongPlay(request, album_id, song_id):
    messages.add_message(request, messages.INFO, 'Hello world.')
    return redirect('music:detail', album_id)
    


def SongDelete(request, album_id, song_id):
    song = Song.objects.get(pk=song_id)
    song.delete()
    return redirect('music:detail', album_id)


def AlbumFavorite(request, pk):
    album_pk = pk
    if request.user is not None:
        selected_album = Album.objects.get(pk=album_pk)
        try:
            favorite_album = request.user.favoritealbum_set.get(
                album=selected_album)
        except (KeyError, FavoriteAlbum.DoesNotExist):
            favorite = FavoriteAlbum()
            favorite.album = Album.objects.get(pk=album_pk)
            favorite.user = request.user
            favorite.save()
        else:
            favorite_album.delete()

    return redirect('music:index')


'''
class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})
	
	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned (normalised) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('music:index')

		return render(request, self.template_name, {'form' : form})
'''
