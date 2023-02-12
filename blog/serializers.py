from rest_framework import serializers
from blog.models import Images
from django.contrib.auth.models import User


class ImagesSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Images
        fields = ('author', 'creator', 'title', 'image')


 #WYŚWIETLANE:
 #creator = author username
 #author = author id
