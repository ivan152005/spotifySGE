from django.db import connection

from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Reestablecer ids de la tabla temporal de los géneros'

    def handle(self, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'bdSpotify_genero';")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))