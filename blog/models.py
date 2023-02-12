from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Images(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to=user_directory_path)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
