from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import CustomAuthTokenLogin


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthTokenLogin.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)