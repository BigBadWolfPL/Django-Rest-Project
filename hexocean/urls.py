from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import ImagesViewSet, CustomAuthTokenLogin


urlpatterns = [
    path(r'', include('blog.urls')),
    path(r'admin/', admin.site.urls),
    path(r'api-token-auth/', CustomAuthTokenLogin.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)