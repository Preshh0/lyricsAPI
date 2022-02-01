from django.urls import path

from lyricsgenerator import views


urlpatterns = [
    path(' ', views.home, name="home" )
]