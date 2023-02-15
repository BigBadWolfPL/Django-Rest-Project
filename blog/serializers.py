from rest_framework import serializers
from blog.models import Images, Profile


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)

class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None,
        use_url=True
    )

    class Meta:
        model = Images
        fields = ['title', 'image']

    def create(self, validated_data):
        return Images.objects.create(**validated_data)
