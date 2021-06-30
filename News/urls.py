from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'News'


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
