from rest_framework import serializers
from blog.models import Images, Profile


class ImagesSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='author.id')
    member = serializers.ReadOnlyField(source='membership')

    class Meta:
        model = Images
        fields = ('author', 'creator','member', 'title', 'image')

