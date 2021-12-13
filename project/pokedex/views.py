from django.http.response import HttpResponse
from pokedex.models import Entrenador, Pokeball, Pokemon
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
    if request.method == 'POST':
        entrenador = Entrenador(
            edad=request.POST['edad'], nombre=request.POST['nombre'])

        entrenador.save()

        return render(request, "pokedex/inicio.html")
        
    return render(request, "pokedex/entrenador.html")


def pokeball(request):
    if request.method == 'POST':
        pokeball = Pokeball(
         nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], color=request.POST['color'])

        pokeball.save()

        return render(request, "pokedex/inicio.html")
    return render(request, "pokedex/pokeball.html")

def buscarPokemon(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        pokemons = Pokemon.objects.filter(nombre__icontains=nombre)

        return render(request, "pokedex/pokemon.html", {"pokemons": pokemons})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def buscarEntrenadores(request):   
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        entrenadores = Entrenador.objects.filter(nombre__icontains=nombre)

        return render(request, "pokedex/entrenador.html", {"entrenadores": entrenadores})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def buscarPokeball(request):   
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        pokeballs = Pokeball.objects.filter(nombre__icontains=nombre)
        return render(request, "pokedex/pokeball.html", {"pokeballs": pokeballs})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)