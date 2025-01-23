from django.core.management import BaseCommand

from bdSpotify.models import Genero, Cancion
'''
class Command(BaseCommand):
    help = 'Migrar clave foránea del género'

    def handle(self, *args, **kwargs):
        try:
            generosTemp = TablaTemporalGenero.objects.all()

            for gt in generosTemp:
                try:
                    a = Genero.objects.get(id=gt.id_genero)
                    c = Cancion.objects.get(id=gt.id_cancion)
                    c.genero = a
                    c.save()
                    self.stdout.write(self.style.SUCCESS(f'Foranea de género añadida a la cancion {c.titulo}'))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error al encontrar la cancion: {e}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
            '''