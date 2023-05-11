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

class TipoInvestigador(BaseModel):
    tipo = models.CharField(max_length=256)

class Investigador(BaseModel):
    usuario = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    tipoinv = models.ForeignKey(TipoInvestigador,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Investigador'
        
class Administrativo(BaseModel):
    cargo = models.CharField(max_length=256)
    date_cargo = models.DateField()
    estado = models.BooleanField()

    class Meta:
        verbose_name = 'Administrativo'        
        
class Universidad(BaseModel):
    nombre = models.CharField(max_length=256)
    departamento = models.CharField(max_length=256)
    pais = models.CharField(max_length=256)
    
class NivelFormacion(BaseModel):
    nombre = models.CharField(max_length=256)
    
class Formacion(BaseModel):
    nombre = models.CharField(max_length=256)
    nivel = models.ForeignKey(NivelFormacion,on_delete=models.CASCADE)

class Docentes(BaseModel):
    inves = models.ForeignKey(Investigador,on_delete=models.CASCADE)
    univ = models.ForeignKey(Universidad,on_delete=models.CASCADE)
    
class Alumnos(BaseModel):
    inves = models.ForeignKey(Investigador,on_delete=models.CASCADE)
    univ = models.ForeignKey(Universidad,on_delete=models.CASCADE)
    programa = models.CharField(max_length=256)
    semestre = models.CharField(max_length=256)