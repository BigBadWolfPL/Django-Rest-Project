from rest_framework import serializers
from blog.models import Images


class ImagesSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Images
        fields = ['image', 'author']

    