from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Images(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to=user_directory_path)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    thumbnail_200 = ImageSpecField(source='image',
                                  processors=[ResizeToFill(100, 200)],
                                  format='JPEG',
                                  options={'quality': 60})
    thumbnail_400 = ImageSpecField(source='image',
                                  processors=[ResizeToFill(100, 400)],
                                  format='JPEG',
                                  options={'quality': 60})


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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()