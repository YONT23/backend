from rest_framework import serializers
from ..models import *

class RevisarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Revisar
        exclude = ('usuario',)
        #fields = '__all__'

class PersonasSerializers(serializers.ModelSerializer):
#   len_nombre = serializers.SerializerMethodField()
    
    class Meta:
        model = Personas
        fields = '__all__'
        
#    def get_len_nombre(self, object):
#        length = len(object.nombre)
#        return length   
    
    def validate(self, data):
       if data['nombre'] == data['apellido']:
           raise serializers.ValidationError("Name and Lastname should be different!")
       else:
           return data 
    
    def validate_nombre(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!") 
        else:
            return value
        
class TipoUsuarioSerializers(serializers.ModelSerializer):
#    len_nombre = serializers.SerializerMethodField()
    
    class Meta:
        model = TipoUsuario
        fields = '__all__'
        
#    def get_len_nombre(self, object):
#        length = len(object.nombre)
#        return length
   
    def validate_nombre(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!") 
        else:
            return value

class UsuariosSerializers(serializers.ModelSerializer):
    #len_username = serializers.SerializerMethodField()
    revisars = RevisarSerializer(many=True, read_only=True)
    
    class Meta:
        model = Usuario
        fields = '__all__'
        
#    def get_len_username(self, object):
#        length = len(object.username)
#        return length
        
    def validate(self, data):
       if data['username'] == data['password']:
           raise serializers.ValidationError("Username and Password should be different!")
       else:
           return data 
    
    def validate_username(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Username is too short!") 
        else:
            return value