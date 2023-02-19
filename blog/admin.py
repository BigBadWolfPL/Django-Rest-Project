from django.contrib import admin
from . import models
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToCover
from imagekit.cachefiles import ImageCacheFile


class AdminThumbnailSpec200(ImageSpec):
    processors = [ResizeToCover(width=40, height=60)]
    options = {'quality': 100 }

def cached_admin_thumb_200(instance):
    cached = ImageCacheFile(AdminThumbnailSpec200(instance.image))
    cached.generate()
    return cached


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'image','admin_thumbnail_200')
    list_filter = ('author', )

    admin_thumbnail_200 = AdminThumbnail(image_field=cached_admin_thumb_200)


@admin.register(models.Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership')
    list_filter = ('membership', )

