from .serializers import RolesSerializers
from rest_framework.serializers import CharField, ModelSerializer, SlugField
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from .customValidators import UserValidatorBefore
User = get_user_model()

#from drf_queryfields import QueryFieldsMixin


class UserSerializersSimple(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserSerializers(ModelSerializer):
    roles = RolesSerializers(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            if (len(representation['roles'])):
                representation['roles'][0] = representation['roles'][0]['id']
            return representation
        except Exception as e:
            return representation

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'roles')


class CreateUserSerializers(ModelSerializer):

    username = SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        validators = [UserValidatorBefore()]


class UserSerializersSimpleRegister(ModelSerializer):
    username = SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        validators = [UserValidatorBefore()]


class UserChangePassword(ModelSerializer):
    password = CharField()

    class Meta:
        model = User
        fields = ('password', 'id')
        validators = [UserValidatorBefore()]
