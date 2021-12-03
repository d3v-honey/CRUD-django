from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import CreateArtistForm, CreateSongForm
from .models import Artist, SongInfo

# Create your views here.
def index(request):
    artist_form = CreateArtistForm()
    song_form = CreateSongForm()


    artists = Artist.objects.all()
    songs = SongInfo.objects.all()

    if request.POST:
        artist_form = CreateArtistForm(request.POST)
        if artist_form.is_valid():
            artist = artist_form.save()
            created_artist = artist_form.cleaned_data.get('name')
            messages.success(request, 'Successfully added ' + created_artist)
            artist_form = CreateArtistForm()

        song_form = CreateSongForm(request.POST)
        if song_form.is_valid():
            song_form.save()
            created_song = song_form.cleaned_data.get('title')
            messages.success(request, 'Successfully added ' + created_song)
            song_form = CreateSongForm()

    context = {
        'artist_form': artist_form,
        'song_form': song_form,
        'artists': artists,
        'songs': songs
    }
    return render(request, 'index.html', context)


def delete_artist(request, _id):
    Artist.objects.filter(id=_id).delete()
    messages.success(request, 'Successfully deleted artist id: '+str(_id))
    return redirect(reverse('song:index'))


def delete_song(request, _id):
    SongInfo.objects.filter(id=_id).delete()
    messages.success(request, 'Successfully deleted song id: '+str(_id))
    return redirect(reverse('song:index'))