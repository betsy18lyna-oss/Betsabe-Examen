from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name='listaspeliculas'),
    path('registrar/', views.registrar_pelicula, name='registrar_pelicula'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('Login/', views.login_usuario, name='Login'),
]
