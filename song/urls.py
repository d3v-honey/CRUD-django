from django.urls import path

from . import views

app_name='song'
urlpatterns = [
    path('', views.index, name="index"),
    path('delete_artist/<int:_id>', views.delete_artist),
    path('delete_song/<int:_id>', views.delete_song),
]