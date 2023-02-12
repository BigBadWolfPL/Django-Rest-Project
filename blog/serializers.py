from rest_framework import serializers
from blog.models import Images

from django.contrib.auth.models import User

class ImagesSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id', write_only=True)

    class Meta:
        model = Images
        fields = ['title', 'image', 'author']

    def validate_author(self, value):
        return self.context['request'].user