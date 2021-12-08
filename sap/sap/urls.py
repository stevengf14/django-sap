from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido, domicilios
from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona
from domicilios.views import detalleDomicilio, editarDomicilio, nuevoDomicilio, eliminarDomicilio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='inicio'),

    # Personas
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona/', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona),

    # Domicilios
    path('domicilios/', domicilios, name='domicilios'),
    path('domicilios/detalleDomicilio/<int:id_domicilio>', detalleDomicilio),
    path('domicilios/editarDomicilio/<int:id_domicilio>', editarDomicilio),
    path('domicilios/nuevoDomicilio/', nuevoDomicilio),
    path('domicilios/eliminarDomicilio/<int:id_domicilio>', eliminarDomicilio),
]

