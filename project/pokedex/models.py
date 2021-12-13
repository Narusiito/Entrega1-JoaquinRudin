from django.db import models


class Pokemon(models.Model):
    """
    Modelo que representa un Pokemon.
    """
    numero = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

class Entrenador(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

class Pokeball(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    color = models.CharField(max_length=15)
