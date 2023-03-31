from ...models import (Document_types, Genders, Persons, Resources, Roles, CustomUser, User_roles, Resources_roles     
                        , Resources_roles, Roles)
from rest_framework.serializers import ModelSerializer, CharField, ValidationError, Serializer, IntegerField
from .user_serializer import UserSerializersSimple

#from ....helps.menuResources import menuResources
#from ....helps.create_response import create_response

from ...mudules import create_response, menuResources





#GENDER
class GenderSerializers(ModelSerializer):
    name = CharField()

    class Meta:
        model = Genders
        exclude = ('createdAt', 'updateAt')
        
#DOCUMENT
class DocumentSerializers(ModelSerializer):
    class Meta:
        model = Document_types
        fields = '__all__'   
                 
#PERSON
class PersonsSerializers(ModelSerializer):
    document_type = DocumentSerializers(read_only=True)
    gender_type = GenderSerializers(read_only=True)
    user = UserSerializersSimple(read_only=True)

    class Meta:
        model = Persons
        fields = '__all__'

class PersonsSimpleSerializers(ModelSerializer):
    document_type = DocumentSerializers(read_only=True)

    class Meta:
        model = Persons
        fields = ('name', 'surname', 'document_type',
                  'phone', 'status', 'date_of_birth')
        
#USER
class UserSerilizers(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
#ROLES
class RolesSerializers(ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name')
        
#RESOURCES
class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources_roles
        fields = '__al__'
        
#ROLES
class RolesSimpleSerializers(ModelSerializer):
    resources = ResourcesSerializers(many=True)

    class Meta:
        model = User_roles
        fields = '__all__'

class RolesUserSerializers(ModelSerializer):
    class Meta:
        model = User_roles
        exclude = ('rolesId',)

    def create(self, validated_data):
        user = validated_data['userId']
        rolesForUser = [User_roles(
            userId=user, rolesId=x) for x in validated_data['roles']]

        try:
            response = User_roles.objects.bulk_create(rolesForUser)
            return response[0]
        except Exception as e:
            response, code = create_response(
                404, '', 'Duplicate Key User - Rol')
            raise ValidationError(response, code=code)
        
#RESOURCES
class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources
        exclude = ('roles',)

class ResourcesRolesSerializers(Serializer):
    rolesId = IntegerField()
    resources = ResourcesSerializers(many=True)

    def create(self, validated_data):
        try:
            resources = []
            list_resources_roles = []

            id_last_resources = 0
            last = Resources.objects.last()
            if last:
                id_last_resources = last.id + 1

            menuResources(validated_data['resources'],
                          resources, Resources, id_last_resources)
            
            resources = Resources.objects.bulk_create(resources)

            roles = Roles.objects.get(pk=validated_data['rolesId'])

            list_resources_roles = [Resources_roles(
                rolesId=roles, resourcesId=r) for r in resources]

            Resources_roles.objects.bulk_create(list_resources_roles)
            return None
        except Exception as e:
            raise e
