from django.core.management import BaseCommand

from bdSpotify.models import Genero, Cancion, TablaTemporalGenero


class Command(BaseCommand):
    help= 'Borrar datos de la tabla temporal'

    def handle(self, *args, **kwargs):
        try:
            TablaTemporalGenero.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Borrados con éxito.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))