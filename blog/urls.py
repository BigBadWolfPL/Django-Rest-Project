from django.urls import path, include
from rest_framework import routers
from blog.views import ImagesViewSet, BinaryImageViewSet


urlpatterns = [
    path(r'', ImagesViewSet.as_view()),
    path(r'binary/', BinaryImageViewSet.as_view({'get': 'list'}),)   
]