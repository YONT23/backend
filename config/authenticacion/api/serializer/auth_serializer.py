from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from .customValidators import UserValidatorBefore
from ...models import CustomUser
from .serializers import RolesSimpleSerializers, PersonsSimpleSerializers
User = get_user_model()


class RegisterSerializers(serializers.ModelSerializer):

    username = serializers.SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = '__all__'
        validators = [UserValidatorBefore()]

    person = PersonsSimpleSerializers(read_only=True)


    def create(self, validated_data):
        #person = validated_data.pop('person')
        user = CustomUser.objects.create(**validated_data)
        #Persons.objects.create(**person, user=user)
        return user


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(label='Email/username')
    password = serializers.CharField()
    roles = RolesSimpleSerializers(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'roles')

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
