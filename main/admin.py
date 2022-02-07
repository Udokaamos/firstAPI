from django.contrib import admin
from main.models import Song
# from django.contrib.auth import get_song_view


# Register your models here
# Song = get_song_view()
admin.site.register(Song)
# admin.site.register(Playlist)