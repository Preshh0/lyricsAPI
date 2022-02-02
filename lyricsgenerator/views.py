from django.shortcuts import render
import requests
from lyricsgenius import Genius
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class GenerateLyrics(APIView):

   def get(self, request, format=None):
      access_token = "hCycsgtQ1zuHku-PtQmxi6NCmWN2aKMwGVcX0tNhhm42JhkiHrR3fY4WLDyfhlhd"
      genius = Genius(access_token, timeout=15, retries=3)
      if genius is not None:
         artist = genius.search_song(title="None", artist="", song_id=378195)
      return Response(artist)
