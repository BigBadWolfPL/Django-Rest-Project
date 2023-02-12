from django.contrib import admin
from . import models


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }