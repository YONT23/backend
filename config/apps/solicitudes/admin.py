from django.contrib import admin
from .models import *

admin.site.register(Autor)
admin.site.register(RolAutor)
admin.site.register(AutorXFormacion)
admin.site.register(AutorXSolicitud)
admin.site.register(Solicitud)
admin.site.register(Seguimiento)
admin.site.register(Anexos)
admin.site.register(PasosSolicitud)
admin.site.register(NivelFormacion)
admin.site.register(ContenidoSolicitud)

admin.site.register(Literatura)
admin.site.register(Artículos)
admin.site.register(Libros)
admin.site.register(Capítuloslibros)



