from django import forms
from django.forms import ModelForm
from .models import SongInfo, Artist

class CreateSongForm(ModelForm):
    class Meta:
        model = SongInfo
        fields = [
            "title",
            "lyrics",
            "album_cover_url",
            "artist_id",
            "year_published"
        ]

class CreateArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = [
            "name",
            "age"
        ]
