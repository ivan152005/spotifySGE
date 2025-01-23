from datetime import datetime

from django.db import models

# Create your models here.


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
class Usuario(models.Model):
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_activo = models.BooleanField(default=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="listas")

    def __str__(self):
        return self.email

class Genero(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=True)
    fecha_creacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nombre}'

class Album(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="albums")
    cantidadCanciones = models.IntegerField(null=True, blank=True)
    duracion = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    oyentes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    # album = models.CharField(max_length=200, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null= True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="canciones", null=True, blank=True)
    duracion = models.IntegerField()
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return f"{self.titulo} - {self.artista}"


class Lista(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="listas")
    canciones = models.ManyToManyField(Cancion, related_name="listas", blank=True)
    fecha_creacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} de {self.usuario.email}"
