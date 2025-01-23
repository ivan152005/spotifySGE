from django.core.management import BaseCommand

from bdSpotify.models import Genero, Cancion


class Command(BaseCommand):
    help = 'Añadir género de las canciones'

    def handle(self, *args, **kwargs):
        if not Genero.objects.exists():
            generos = Cancion.objects.values_list('genero', flat=True).distinct()
            for genero in generos:
                Genero.objects.create(nombre=genero)
                self.stdout.write(self.style.SUCCESS('Género añadido con éxito'))
        else:
            self.stdout.write(self.style.SUCCESS('Los géneros ya están añadidos'))