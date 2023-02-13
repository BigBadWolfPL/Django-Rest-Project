from rest_framework import serializers
from blog.models import Images, Profile


class ImagesSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='author.username')
    profile = Images.objects.all()[0]

    class Meta:
        model = Images
        fields = ('author', 'creator', 'title', 'image')


profile = Images.objects.all()[0]
print(profile.thumbnail_200.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg



print(f'WIDTH: {profile.thumbnail_200.width}')
print(f'HEIGHT: {profile.thumbnail_200.height}')

print(f'WIDTH: {profile.thumbnail_400.width}')
print(f'HEIGHT: {profile.thumbnail_400.height}')