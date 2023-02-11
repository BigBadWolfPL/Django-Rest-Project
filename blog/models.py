from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#class Post(models.Model):
#    title = models.CharField(max_length=100)
#    content = models.TextField()
#    date_posted = models.DateTimeField(default=timezone.now)
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.title



def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Post(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to=user_directory_path)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
