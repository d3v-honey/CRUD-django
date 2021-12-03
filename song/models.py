from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SongInfo(models.Model):
    title = models.CharField(max_length=45)
    lyrics = models.TextField()
    album_cover_url = models.CharField(max_length=500)
    artist_id = models.ForeignKey(
        Artist, related_name="artist", on_delete=models.CASCADE
    )
    year_published = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
