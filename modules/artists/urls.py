from django.conf.urls import url
from .views import ListArtist

urlpatterns = [
    url(r'^artist/$', ListArtist.as_view(), name="listArtist"),
]
