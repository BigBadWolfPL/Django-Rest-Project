from rest_framework import viewsets
from blog.serializers import ImagesSerializer
from blog.models import Images
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

class ImagesViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    def get_queryset(self):

        user = self.request.user
        return Images.objects.filter(author=user)
