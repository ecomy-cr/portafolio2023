from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.perfil, name='perfil'),
    path('portafolio/', views.portafolio, name='portafolio'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)