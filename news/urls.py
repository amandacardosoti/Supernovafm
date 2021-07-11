from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news, name='news'),
    path('noticias/', views.noticias, name='noticias'),
    path('programacao/', views.programacao, name='programacao'),
    path('contato/', views.contato, name='contato'),
    path('noticia1/', views.noticia1, name='noticia1'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
