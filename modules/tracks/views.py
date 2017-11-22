from rest_framework import viewsets, filters
from .models import Track
from .serializers import TrackModelSerializer, TrackAlbumSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class TrackViewSet(viewsets.ModelViewSet):
    "Endpoint que trae todos los tracks"

    serializer_class = TrackModelSerializer
    queryset = Track.objects.all().select_related('album')
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('raiting', 'duration')
    search_fields = ('name', 'album__name')
