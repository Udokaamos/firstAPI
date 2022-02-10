from django.urls import path
from . import views 

# urlpatterns = [
#     path('songs/', views.song_view, name="songs"),
    
#     path('songs/<int:song_id>/', views.profile_view, name="profile"),

#     path('playlists/', views.song_view, name="playlists"),

# ]

urlpatterns = [
    path("songs/", views.songs),
    path("songs/<int:song_id>/", views.song_detail),
    path("playlists/", views.playlists),
    path("playlists/<int:item_id>/", views.playlist_detail),
]