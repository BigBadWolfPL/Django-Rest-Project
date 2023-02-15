from rest_framework import serializers
from blog.models import Images, Profile


#class ImagesSerializer(serializers.ModelSerializer):
#    image = serializers.ImageField(
#        max_length=None,
#        use_url=True
#    )
#    
#    class Meta:
#        model = Images
#        fields = ['image']
#
#    def create(self, validated_data):
#        return Images.objects.create(**validated_data)



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'