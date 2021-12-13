from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('pokeball/', views.pokeball, name='pokeball'),
    path('entrenador/', views.entrenador, name='entrenador'),
]