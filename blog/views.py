from blog.serializers import ImagesSerializer, BinaryImageSerializer
from blog.models import Images, BinaryImage
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework import generics
from rest_framework import viewsets
from django.conf import settings
import base64
#from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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
                content['binary_data_link'] = '/binary/'
        return Response(content)


class BinaryImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = BinaryImage.objects.all()
    serializer_class = BinaryImageSerializer

    def get_queryset(self):
        return BinaryImage.objects.filter(id=self.request.user.pk).all()


class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user_name': user.username
        })