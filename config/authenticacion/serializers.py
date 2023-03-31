from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from rest_framework.serializers import CharField, ModelSerializer, SlugField

#from .api.serializer.serializers import RolesSerializers
from .api.serializer.customValidators import UserValidatorBefore
User = get_user_model()

#class UserChangePassword(ModelSerializer):
#    password = CharField()
#
#    class Meta:
#        model = User
#        fields = ('password', 'id')
#        validators = [UserValidatorBefore()]

#class UserSerializersSimple(ModelSerializer):
#    class Meta:
#        model = User
#        fields = ('username', 'email')

#class CreateUserSerializers(ModelSerializer):
#
#    username = SlugField(
#        max_length=100,
#        validators=[UniqueValidator(queryset=User.objects.all())]
#    )
#
#    class Meta:
#        model = User
#        fields = ('username', 'password', 'email')
#        validators = [UserValidatorBefore()]
#
#class UserSerializersSimpleRegister(ModelSerializer):
#    username = SlugField(
#        max_length=100,
#        validators=[UniqueValidator(queryset=User.objects.all())]
#    )
#
#    class Meta:
#        model = User
#        fields = ('username', 'password', 'email', 'first_name', 'last_name')
#        validators = [UserValidatorBefore()]

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    avatar = serializers.ImageField(
        required=False, allow_null=True) 

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'avatar') 
        
def validate_password(self, value):
    return make_password(value)

def validate_username(self, value):
    value = value.replace(" ", "")  # Ya que estamos borramos los espacios
    try:
        user = get_user_model().objects.get(username=value)
        # Si es el mismo usuario mandando su mismo username le dejamos
        if user == self.instance:
            return value
    except get_user_model().DoesNotExist:
        return value
    raise serializers.ValidationError("Nombre de usuario en uso") 

def validate_email(self, value):
    # Hay un usuario con este email ya registrado?
    try:
        user = get_user_model().objects.get(email=value)
    except get_user_model().DoesNotExist:
        return value
    # En cualquier otro caso la validación fallará
    raise serializers.ValidationError("Email en uso")