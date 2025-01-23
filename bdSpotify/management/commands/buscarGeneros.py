from django.core.management import BaseCommand

from bdSpotify.models import Cancion


class Command(BaseCommand):
    help='Buscar canciones por género'

    def add_arguments(self, parser):
        parser.add_argument('--nombre',
                            type = str,
                            help='nombre categoria',
                            required=False)

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Buscado realizado con éxito'))

        if kwargs:
            canciones = Cancion.objects.all()
            for i in canciones:
                self.stdout.write(self.style.SUCCESS(f'canción: {i}'))
