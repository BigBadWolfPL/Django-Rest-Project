from rest_framework import viewsets
from blog.serializers import ImagesSerializer
from blog.models import Images, Profile
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ImagesViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    
    def get(self, request, format=None):
        user = self.request.user
        membership = user.profile.membership

        small_images_links =[str(img.thumbnail_200.url) for img in Images.objects.filter(author=user)]
        medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.filter(author=user)]
        #small_images_links = profile.thumbnail_200.url                            #small_images = Images.objects.filter(author=user).values('id', 'image')
        #medium_images_links = profile.thumbnail_400.url                           #medium_images = Images.objects.filter(author=user).values('id', 'image')


        content = {
            'user': str(request.user),
            'small_images_links': small_images_links,
            'medium_images_links': medium_images_links,
            'membership_BASIC': membership == "BASIC",
            'membership_PREMIUM': membership == "PREMIUM",
            'membership_ENTERPRISE': membership == "ENTERPRISE",
        }

        return Response(content)

    def post(self, request, format=None):
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



########################################################################
########################################################################

print('\n\n')


#print(Profile.objects.filter(id=1))
#user_obj = User.objects.filter(id=2).first()
#profile_obj = Profile.objects.all().first()
#print(profile_obj.membership)
#print(profile_obj.user)
#print(user_obj == profile_obj.user)
#filtered = Images.objects.filter(author=2)
#print(filtered)

#profile = Images.objects.all()
#print(profile.thumbnail_200.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
#print(profile.thumbnail_400.url)
#
#
#print(f'WIDTH: {profile.thumbnail_200.width}')
#print(f'HEIGHT: {profile.thumbnail_200.height}')
#
#print(f'WIDTH: {profile.thumbnail_400.width}')
#print(f'HEIGHT: {profile.thumbnail_400.height}')


print('\n\n')