from django.contrib import admin

from .models import SitePhotos, Video


# Register your models here.

@admin.register(SitePhotos)
class SitePhotosAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
