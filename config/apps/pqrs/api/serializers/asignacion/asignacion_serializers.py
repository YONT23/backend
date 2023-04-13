from rest_framework import serializers
from ....models import Asignacion, CustomUser, Pqrs
from ..BaseSerializers import BaseSerializers

class AsignacionSerializers(BaseSerializers):
    funcionarioId = serializers.SlugRelatedField("username",read_only=True)
    pqrs = serializers.SlugRelatedField("description",read_only=True)


    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        try:
            funcionarioId = CustomUser.objects.get(pk=validated_data["funcionarioId"])
            pqrs = Pqrs.objects.get(pk=validated_data["pqrs"])
            userCreate = None
            if "userCreate" in validated_data:
                userCreate = validated_data["userCreate"]
            return Asignacion.objects.create(funcionarioId=funcionarioId,pqrs=pqrs,userCreate=userCreate)
        except (CustomUser.DoesNotExist,Pqrs.DoesNotExist) as e:
            raise serializers.ValidationError(e.args[0])

    def update(self, instance, validated_data):
        try:
            newfuncionarioId = CustomUser.objects.get(pk=validated_data["funcionarioId"])
            instance.funcionarioId = newfuncionarioId
            instance.userUpdate = validated_data.get("userUpdate",instance.userUpdate)
            instance.save()
            return instance
        except CustomUser.DoesNotExist as e:
            raise serializers.ValidationError(e.args[0])
    
    
        
