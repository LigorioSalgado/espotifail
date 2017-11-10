from django.conf.urls import url
from .views import ListArtist, DetailArtist

urlpatterns = [
    url(r'^artists/$', ListArtist.as_view(), name="listArtist"),
    url(r'^artists/(?P<id>[0-9a-f-]+)/$',
        DetailArtist.as_view(), name="detailArtist"),
]
