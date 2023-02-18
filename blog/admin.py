from django.contrib import admin
from . import models
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToCover
from imagekit.cachefiles import ImageCacheFile


class AdminThumbnailSpec200(ImageSpec):
    processors = [ResizeToCover(width=100, height=200)]
    options = {'quality': 100 }

def cached_admin_thumb_200(instance):
    cached = ImageCacheFile(AdminThumbnailSpec200(instance.image))
    cached.generate()
    return cached

class AdminThumbnailSpec400(ImageSpec):
    processors = [ResizeToCover(width=100, height=400)]
    options = {'quality': 100 }

def cached_admin_thumb_400(instance):
    cached = ImageCacheFile(AdminThumbnailSpec400(instance.image))
    cached.generate()
    return cached


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'image','admin_thumbnail_200', 'admin_thumbnail_400')
    list_filter = ('author', )

    admin_thumbnail_200 = AdminThumbnail(image_field=cached_admin_thumb_200)
    admin_thumbnail_400 = AdminThumbnail(image_field=cached_admin_thumb_400)


@admin.register(models.Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership')
    list_filter = ('membership', )

