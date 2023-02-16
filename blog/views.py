from blog.serializers import ImagesSerializer
from blog.models import Images
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


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
            small_images_links =[str(img.thumbnail_200.url) for img in Images.objects.all()]  # Tylko do podglądu >>> należy się zalogować w postman
            medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.all()]
        else:
            user = self.request.user
            membership = user.profile.membership #trzeba się zalogować w postman bo wywala błąd (AnonymousUser ...) stąd ten warunek if/ else
            small_images_links =[str(img.thumbnail_200.url) for img in Images.objects.filter(author=user)]
            medium_images_links =[str(img.thumbnail_400.url) for img in Images.objects.filter(author=user)]

        content = {
            'user': str(request.user),
            'small_images_links': small_images_links,
            'medium_images_links': medium_images_links,
            'membership_None': f"{user}",
            #'membership_BASIC': membership == "BASIC",
            #'membership_PREMIUM': membership == "PREMIUM",
            #'membership_ENTERPRISE': membership == "ENTERPRISE",
        }
        return Response(content)
