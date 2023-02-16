from rest_framework import viewsets
from blog.serializers import ImagesSerializer
from blog.models import Images, Profile
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
import json

class ImagesViewSet(APIView):
    #permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format=None):
        #user = self.request.user
        #membership = user.profile.membership

        #small_images_links =[str(img.thumbnail_200.url) for img in Images.objects.filter(author=user)]
        #medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.filter(author=user)]

        content = {
            'user': str(request.user),
            #'small_images_links': small_images_links,
            #'medium_images_links': medium_images_links,
            #'membership_BASIC': membership == "BASIC",
            #'membership_PREMIUM': membership == "PREMIUM",
            #'membership_ENTERPRISE': membership == "ENTERPRISE",
        }
        return Response(content)

    def post(self, request, format=None):
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)