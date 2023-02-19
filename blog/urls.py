from django.urls import path, include
from blog.views import ImagesView, BinaryImageView


urlpatterns = [
    path('', ImagesView.as_view()),
    path('binary/', BinaryImageView.as_view()), 
]