from django.urls import path
from . import views

urlpatterns = [
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_review/', views.crear_review, name='crear_review'),
    path('listar_libros/', views.listar_libros, name='listar_libros'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('listar_reviews/', views.listar_reviews, name='listar_reviews'),
]