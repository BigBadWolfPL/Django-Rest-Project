from rest_framework import routers
from blog.views import ImagesViewSet


router = routers.DefaultRouter()
router.register(r'blog', ImagesViewSet)