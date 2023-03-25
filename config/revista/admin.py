from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Personas)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Revisar)