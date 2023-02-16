from django.urls import path, include
from rest_framework import routers
from blog.views import ImagesViewSet, AddImageViewSet


#router = routers.DefaultRouter()
#router.register(r'blog', ImagesViewSet)


urlpatterns = [
    path('', ImagesViewSet.as_view()),
    path('add/', AddImageViewSet.as_view())   
]