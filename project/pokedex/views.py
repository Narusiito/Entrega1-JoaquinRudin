from pokedex.models import Pokemon
from django.shortcuts import render


def index(request):
    return render(request, "pokedex/inicio.html")


def pokemon(request):
    if request.method == 'POST':
        pokemon = Pokemon(
            numero=request.POST['numero'], nombre=request.POST['nombre'], tipo=request.POST['tipo'])

        pokemon.save()

        return render(request, "pokedex/inicio.html")

    return render(request, "pokedex/pokemon.html")


def entrenador(request):
    return render(request, "pokedex/entrenador.html")


def pokeball(request):
    return render(request, "pokedex/pokeball.html")
