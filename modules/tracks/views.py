from rest_framework import viewsets
from .models import Track
from .serializers import TrackModelSerializer, TrackAlbumSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TrackViewSet(viewsets.ModelViewSet):

    serializer_class = TrackModelSerializer
    queryset = Track.objects.all().select_related('album')
    permission_classes = (IsAuthenticated,)
