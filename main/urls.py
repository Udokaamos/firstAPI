from django.urls import path
from . import views 

urlpatterns = [
    path('songs/', views.song_view, name="songs"),
    
    path('songs/<int:song_id>/', views.profile_view, name="profile")

]