from django.urls import path, include
from rest_framework import routers
from blog.views import ImagesViewSet, BinaryImageView


urlpatterns = [
    path('', ImagesViewSet.as_view()),
    path('binary/', BinaryImageView.as_view(),)   
]