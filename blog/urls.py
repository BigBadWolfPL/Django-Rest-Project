from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import ImagesViewSet


urlpatterns = [
    path('', ImagesViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)