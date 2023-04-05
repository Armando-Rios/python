
from django.urls import path
from .views import lista_directores, detalle_director, peliculas_director

urlpatterns = [
    path('', lista_directores, name='lista_directores'),
    path('<int:director_id>/', detalle_director, name='detalle_director'),
    path('<int:director_id>/peliculas/',
         peliculas_director, name='peliculas_director'),
]
