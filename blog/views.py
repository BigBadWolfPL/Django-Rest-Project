from blog.serializers import ImagesSerializer
from blog.models import Images
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework import generics


class ImagesViewSet(APIView):
    #permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        if self.request.user.id is None:
            user = f"{self.request.user} --> PLEASE LOGIN // PROSZĘ SIĘ ZALOGOWAĆ ;) <--"
            oryginal_size = [str(img.thumbnail_oryginal.url) for img in Images.objects.all()] # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            small_images_links =[str(img.thumbnail_200.url) for img in Images.objects.all()]  # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.all()] # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            
            content = {
            'user': str(request.user), # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            'small_images_links': small_images_links, # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            'medium_images_links': medium_images_links, # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            'oryginal_size': oryginal_size, # Tylko do podglądu // usunąć >>> należy się zalogować w postman
            'membership_None': f"{user}",
            }
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
                binary_images_links = [str(img.thumbnail_binary.url) for img in Images.objects.filter(author=user)] #"link to binary here ..."
                content['medium_images_links'] = medium_images_links
                content['oryginal_size'] = oryginal_size
                content['binary_images_links'] = binary_images_links


        return Response(content)


class AddImageViewSet(generics.CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
