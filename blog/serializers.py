from rest_framework import serializers
from blog.models import Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['image', 'author']