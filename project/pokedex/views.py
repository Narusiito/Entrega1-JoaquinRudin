from django.http import HttpResponse


def index(request):
    return HttpResponse("Vista principal.")


def pokemon(request):
    return HttpResponse("Vista Pokemon.")


def entrenador(request):
    return HttpResponse("Vista Entrenador.")


def pokeball(request):
    return HttpResponse("Vista Pokeball.")
