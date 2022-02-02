from django.urls import path

from .views import GenerateLyrics


urlpatterns = [
    path('home/', GenerateLyrics.as_view(), name="home" )
]