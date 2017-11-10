from django.shortcuts import render
from rest_framework import generics
from .models import Album
from .serializers import AlbumModelSerializer

# Create your views here.


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


class DetailGenericAlbum(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
