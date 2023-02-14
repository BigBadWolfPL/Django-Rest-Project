from rest_framework import serializers
from blog.models import Images, Profile




class ImagesSerializer(serializers.Serializer):

    #creator = serializers.ReadOnlyField(source='author.username')
    #profile = Images.objects.all()

    class Meta:
        model = Images
        fields = '__all__'




#class ImagesSerializer(serializers.ModelSerializer):
#
#    creator = serializers.ReadOnlyField(source='author.username')
#    profile = Images.objects.all()[0]
#
#    class Meta:
#        model = Images
#        fields = ('author', 'creator', 'title', 'image')
