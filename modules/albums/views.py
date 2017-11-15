from django.shortcuts import render
from rest_framework import generics, filters
from .models import Album
from .serializers import AlbumModelSerializer, AlbumTracksSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import GroupAPermissions
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumTracksSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('country', 'currency', 'price')
    search_fields = ('name', 'genre')
    #permission_classes = (IsAuthenticated, GroupAPermissions)


class DetailGenericAlbum(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
