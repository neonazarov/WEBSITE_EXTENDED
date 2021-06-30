from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from News import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('News.urls', 'NEWS')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
