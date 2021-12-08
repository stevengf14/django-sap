from django.contrib import admin

# Register your models here.
from personas.models import Persona
from personas.models import Domicilio

admin.site.register(Persona)
admin.site.register(Domicilio)