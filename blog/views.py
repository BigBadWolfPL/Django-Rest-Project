from blog.serializers import ImagesSerializer, BinaryImageSerializer
from blog.models import Images, BinaryImage
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework import generics
from django.conf import settings
import base64
from rest_framework.renderers import JSONRenderer


class ImagesViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ImagesSerializer

    def post(self, request, format=None):
        serializer = ImagesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        if self.request.user.id is None:
            content = {'PLEASE LOGIN': f"{self.request.user} // PLEASE LOGIN // PROSZĘ SIĘ ZALOGOWAĆ ;) //"}

        else:
            ### BASIC MEMBERSHIP ###
            user = self.request.user
            membership = user.profile.membership
            small_images_links =[str(img.thumbnail_200.url) for img in Images.objects.filter(author=user)]
            content = {
                'user': str(request.user),
                'your_membership': membership,
                'small_images_links': small_images_links,
                }
            ### PREMIUM MEMBERSHIP ###
            if membership == "PREMIUM":
                medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.filter(author=user)]
                oryginal_size = [str(img.thumbnail_oryginal.url) for img in Images.objects.filter(author=user)]
                content['medium_images_links'] = medium_images_links
                content['oryginal_size'] = oryginal_size
            ### ENTERPRISE MEMBERSHIP ###
            if membership == "ENTERPRISE":
                medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.filter(author=user)]
                oryginal_size = [str(img.thumbnail_oryginal.url) for img in Images.objects.filter(author=user)]
                binary_objects = BinaryImage.objects.filter(id=user.id)
                binary_data_serializer = BinaryImageSerializer(binary_objects, many=True)
                binary_data = binary_data_serializer.data

                content['medium_images_links'] = medium_images_links
                content['oryginal_size'] = oryginal_size
                content['binary_data'] = binary_data
        return Response(content)


class BinaryImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        if self.request.user.id is None:
            content = {'PLEASE LOGIN': f"{self.request.user} // PLEASE LOGIN // PROSZĘ SIĘ ZALOGOWAĆ ;) //"}
        else:
            ### BASIC MEMBERSHIP ###
            user = self.request.user
            membership = user.profile.membership
            content = {
                'binary': f'Needed ENTERPRISE membership to access this data - Your membership is: {membership}.',
                }
            ### ENTERPRISE MEMBERSHIP ###
            if membership == "ENTERPRISE":
                binary_objects = BinaryImage.objects.filter(id=user.id)
                serializer = BinaryImageSerializer(binary_objects, many=True)
                content = serializer.data
        return Response(content)
