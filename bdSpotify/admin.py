from django.contrib import admin
from .models import Plan, Usuario, Cancion, Genero, TablaTemporalGenero
# Register your models here.
admin.site.register(Plan)
admin.site.register(Usuario)
admin.site.register(Cancion)
admin.site.register(Genero)
admin.site.register(TablaTemporalGenero)

