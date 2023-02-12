from rest_framework import viewsets

from blog.serializers import ImagesSerializer
from blog.models import Images

# Create your views here.

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


