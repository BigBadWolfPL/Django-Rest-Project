from rest_framework import serializers
from blog.models import Images, BinaryImage


class ImagesSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Images
        fields = ['image', 'author', 'time']


class BinaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinaryImage
        fields = '__all__'

