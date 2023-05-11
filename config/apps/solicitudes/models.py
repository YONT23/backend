from django.db import models
from django.contrib.auth import get_user_model
from apps.authenticacion.models import CustomUser

CustomUser = get_user_model()


class BaseModel(models.Model):
    createdAt = models.DateField(auto_now_add=True,blank=True, null=True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    userUpdate = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name="+")
    
    class Meta:
        abstract = True

class RolAutor(BaseModel):
    nombre = models.CharField(max_length=256)

class Autor(BaseModel):
    usuario = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Autor'
        
class Solicitud(BaseModel):
    fecha = models.DateField()
    urls = models.CharField(max_length=256)
    orcid = models.CharField(max_length=256)
    afiliacion = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Solicitud'   
             
class PasosSolicitud(BaseModel):
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
    responsable = models.CharField(max_length=256)
    nivel = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'PasosSolicitud'        
        
class Seguimiento(BaseModel):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    pasos_solicitud = models.ForeignKey(PasosSolicitud,on_delete=models.CASCADE)
    
class Artículos(BaseModel):
    apellidos_autor = models.CharField(max_length=256)
    inicial_nombre = models.CharField(max_length=256)
    año = models.CharField(max_length=256)
    titulo = models.CharField(max_length=256)
    revista = models.CharField(max_length=256)
    volumen = models.CharField(max_length=256)
    paginas = models.CharField(max_length=256)
    doi = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    
class Libros(BaseModel):
    apellidos_autor = models.CharField(max_length=256)
    inicial_nombre = models.CharField(max_length=256)
    año = models.CharField(max_length=256)
    titulo = models.CharField(max_length=1000)
    Editorial = models.CharField(max_length=256)
    doi = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    
class Capítuloslibros(BaseModel):
    apellidos_autor = models.CharField(max_length=256)
    inicial_nombre = models.CharField(max_length=256)
    año_publicacion = models.CharField(max_length=256)
    titulo_capitulo = models.CharField(max_length=1000)
    inicial_editorcompilador = models.CharField(max_length=256)
    editorcompilador_libro = models.CharField(max_length=256)
    Título_libro = models.CharField(max_length=1000)
    Editorial = models.CharField(max_length=256)
    
class Literatura(BaseModel):
    articulo = models.ForeignKey(Artículos,on_delete=models.CASCADE)
    libros = models.ForeignKey(Libros,on_delete=models.CASCADE)
    capitulos = models.ForeignKey(Capítuloslibros,on_delete=models.CASCADE)
    
class ContenidoSolicitud(BaseModel):
    resumen = models.CharField(max_length=1500)
    palabras_claves = models.CharField(max_length=256)
    abstract = models.CharField(max_length=256)
    Keywords = models.CharField(max_length=256)
    introduccion = models.CharField(max_length=2000)
    materi_metodos = models.CharField(max_length=2000)
    result_discu = models.CharField(max_length=2000)
    agradecimientos = models.CharField(max_length=1500)
    literact_citada = models.ForeignKey(Literatura,on_delete=models.CASCADE)
    
class Anexos(BaseModel):
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE)

class AutorXSolicitud(BaseModel):
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud,on_delete=models.CASCADE)
    rol_autor = models.ForeignKey(RolAutor,on_delete=models.CASCADE)
    
class NivelFormacion(BaseModel):
    nombre = models.CharField(max_length=256)
    
class AutorXFormacion(BaseModel):
    nombre = models.CharField(max_length=256)
    fecha_grado = models.CharField(max_length=256)
    resol_conv = models.CharField(max_length=256)
    cert_grado = models.CharField(max_length=256)
    cert_resol = models.CharField(max_length=256)
    nivel_formacion = models.ForeignKey(NivelFormacion,on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
