from django.contrib import admin
from . import models


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')

admin.site.register(models.Profile)