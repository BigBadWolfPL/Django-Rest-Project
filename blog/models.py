from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Images(models.Model):

    image = models.ImageField(_("Image"), upload_to=user_directory_path)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    thumbnail_oryginal = ImageSpecField(source='image',
                                  options={'quality': 100})
    thumbnail_200 = ImageSpecField(source='image',
                                  processors=[ResizeToCover(width=True, height=200)],
                                  options={'quality': 100})
    thumbnail_400 = ImageSpecField(source='image',
                                  processors=[ResizeToCover(width=True, height=400)],
                                  options={'quality': 100})
    #thumbnail_binary = ImageSpecField(source='image', options={'quality': 100})    # do wywalenia

    def __str__(self):
        return f'{self.author} {self.image}'

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


#class BinaryImage(models.Model):                                   # prawdopodobnie do wywalenia
#    author = models.ForeignKey(User, on_delete=models.CASCADE)     # prawdopodobnie do wywalenia
#    binary_img = models.BinaryField(blank=True)                    # prawdopodobnie do wywalenia


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()