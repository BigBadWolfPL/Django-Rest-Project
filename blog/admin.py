from django.contrib import admin
#from . import models


#@admin.register(models.Images)
#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('id', 'author')
#
#admin.site.register(models.Profile)


from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToCover
from imagekit.cachefiles import ImageCacheFile

from .models import Images, Profile

class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToCover(width=100, height=30)]
    #format = 'JPEG'
    options = {'quality': 100 }

def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.image))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field=cached_admin_thumb)

admin.site.register(Images, PhotoAdmin)
admin.site.register(Profile)