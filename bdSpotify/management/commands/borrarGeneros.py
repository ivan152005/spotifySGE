from django.core.management import BaseCommand

from bdSpotify.models import Genero


class Command(BaseCommand):
    help = 'Borrar géneros'

    def handle(self, *args, **kwargs):
        try:
            Genero.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Géneros borrados con éxito.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))