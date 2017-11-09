from django.contrib import admin
from .models import Artist

# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
