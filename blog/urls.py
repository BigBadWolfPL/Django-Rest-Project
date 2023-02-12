from django.urls import path, include
from rest_framework import routers
from blog.views import ImagesViewSet


router = routers.DefaultRouter()
router.register(r'blog', ImagesViewSet)

#urlpatterns = [
#    path('api-auth/', include('rest_framework.urls'))
#]