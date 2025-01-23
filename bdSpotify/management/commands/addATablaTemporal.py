from django.core.management import BaseCommand

from bdSpotify.models import Genero, Cancion, TablaTemporalGenero

class Command(BaseCommand):
    help = 'Añadir género a canciones'

    def handle(self, *args, **kwargs):
        try:
            # Recojo todas las canciones
            cancion = Cancion.objects.all()
            for c in cancion:
                # Busco el genero por cancion
                genero = Genero.objects.get(nombre=c.genero)
                TablaTemporalGenero.objects.create(id_genero=genero.id, id_cancion=c.id)

                self.stdout.write(self.style.SUCCESS(f'Cancion: {str(c.titulo)}. Genero: {c.genero}'))
                self.stdout.write(self.style.SUCCESS(f'Tabla temporal añadida con éxito'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error al guardar en la tabla temporal'))

