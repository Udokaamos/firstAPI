from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_view, name="users")

]