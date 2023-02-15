from rest_framework import serializers
from blog.models import Images, Profile


class ImagesSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    def create(self, validated_data):
        return Images.objects.create(**validated_data)
