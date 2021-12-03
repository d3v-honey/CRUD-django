
from django.contrib import admin
from .models import Artist, SongInfo


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
        "created_at",
        "updated_at",
    )


class SongInfoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        # "lyrics",
        "album_cover_url",
        "artist_id",
        "year_published",
        "created_at",
        "updated_at"
    )


admin.site.register(Artist, ArtistAdmin)
admin.site.register(SongInfo, SongInfoAdmin)