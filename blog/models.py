from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Images(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to=user_directory_path)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Profile(models.Model):

    MEMBERSHIP = (
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.CharField(max_length=10, choices=MEMBERSHIP, default='BASIC')

    def __str__(self):
        return f'{self.user.username} {self.membership}'


