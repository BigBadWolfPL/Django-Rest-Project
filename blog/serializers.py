from rest_framework import serializers
from blog.models import Images

from django.contrib.auth.models import User


class ImagesSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Images
        fields = ('id','author','creator', 'title', 'image')



#class ImagesSerializer(serializers.HyperlinkedModelSerializer):
#
#    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id', write_only=True)
#
#    class Meta:
#        model = Images
#        fields = ['id', 'title', 'image', 'author']
#
#    #def validate_author(self, value):
#    #    return self.context['request'].user




