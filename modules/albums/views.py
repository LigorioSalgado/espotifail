from django.shortcuts import render
from rest_framework import generics
from .models import Album
from .serializers import AlbumModelSerializer, AlbumTracksSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import GroupAPermissions
# Create your views here.


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumTracksSerializer
    permission_classes = (IsAuthenticated, GroupAPermissions)


class DetailGenericAlbum(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
