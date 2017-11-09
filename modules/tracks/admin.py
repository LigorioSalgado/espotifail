from django.contrib import admin
from .models import Track
# Register your models here.


class TrackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Track, TrackAdmin)
