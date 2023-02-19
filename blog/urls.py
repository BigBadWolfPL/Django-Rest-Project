from django.urls import path, include
from rest_framework import routers
from blog.views import ImagesViewSet, BinaryImageView


urlpatterns = [
    path(r'', ImagesViewSet.as_view()),
    path(r'binary/', BinaryImageView.as_view(),)   
]