from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import base64


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Images(models.Model):
    image = models.ImageField(_("Image"), upload_to=user_directory_path)
    time = models.IntegerField(blank=True, help_text = "Token Lifetime in seconds (min= 300 / max=30000, This field is optional >>> default=300)", default=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    thumbnail_oryginal = ImageSpecField(source='image',
                                  options={'quality': 100})
    thumbnail_200 = ImageSpecField(source='image',
                                  processors=[ResizeToCover(width=True, height=200)],
                                  options={'quality': 100})
    thumbnail_400 = ImageSpecField(source='image',
                                  processors=[ResizeToCover(width=True, height=400)],
                                  options={'quality': 100})
    def __str__(self):
        return f'{self.author} {self.image} {self.time}'


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


class BinaryImage(models.Model):
    binary = models.BinaryField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Images)
def create_binary_data(sender, instance, created, **kwargs):
    if created:
        with open(settings.MEDIA_ROOT +'/'+ str(instance.image), 'rb') as f:
            file = f.read()
            bytes_obj = base64.b64encode(file)
            BinaryImage.objects.update_or_create(binary=bytes_obj)
