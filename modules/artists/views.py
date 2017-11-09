from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Artist
from .serializers import ArtistsModelSerializer
# Create your views here.


class ListArtist(APIView):

    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistsModelSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailArtist(APIView):

    def get(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
