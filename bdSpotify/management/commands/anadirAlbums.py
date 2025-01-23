from django.core.management.base import BaseCommand
from bdSpotify.models import *
import random

class Command(BaseCommand):
    help = "Añadir álbumes sin repetir y asignarlos a las canciones"

    def handle(self, *args, **kwargs):
        usuarios = Usuario.objects.all()
        if not usuarios.exists():
            self.stdout.write(self.style.ERROR("No hay usuarios en la base de datos"))
        else:
            
            canciones = Cancion.objects.all()
            albums_creados = {}

            for cancion in canciones:
                album_nombre = cancion.album

                if album_nombre not in albums_creados:
                    album_obj, creado = Album.objects.get_or_create(
                        nombre=album_nombre,
                        defaults={
                            "descripcion": f"Álbum {album_nombre} con una colección de canciones",
                            "usuario": random.choice(usuarios),
                            "oyentes": random.randint(1000, 100000000),
                            "cantidadCanciones": 0,
                            "duracion": 0
                        }
                    )
                    albums_creados[album_nombre] = album_obj
                else:
                    album_obj = albums_creados[album_nombre]

                cancion.albumTemporal = album_obj
                cancion.save()


            for album_nombre, album_obj in albums_creados.items():
                canciones_del_album = Cancion.objects.filter(albumTemporal=album_obj)
                album_obj.cantidadCanciones = canciones_del_album.count()
                album_obj.duracion = sum(c.duracion for c in canciones_del_album)
                album_obj.save()

            self.stdout.write(self.style.SUCCESS("Se han añadido los álbumes correctamente y se han asignado a las canciones."))