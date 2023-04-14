from apps.authenticacion.models import Roles
from ....serializer.serializers import RolesSerializers
from .....mudules import (CreateAPIView, ListAPIView, Response, UpdateAPIView,
                       create_response, status, DestroyAPIView, IsAdminRole)

class RolesListView(ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = RolesSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Roles', serializers.data)
        return Response(response, status=code)

class RolescreateView(CreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def post(self, request, *args, **kwargs):
        roleSerializers = RolesSerializers(data=request.data)
        if roleSerializers.is_valid():
            roleSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Role', roleSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', roleSerializers.errors)
        return Response(response, status=code)

class RoleUpdateView(UpdateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Roles.objects.get(id=pk)
        except Roles.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        role = self.get_object()
        if role is None:
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'Role Not Exist')
            return Response(response, status=code)

        try:
            roleSerializers = RolesSerializers(role, data=request.data)
            if roleSerializers.is_valid():
                roleSerializers.save()
                response, code = create_response(
                    status.HTTP_200_OK, 'Role', roleSerializers.data)
                return Response(response, status=code)
            response, code = create_response(
                status.HTTP_200_OK, 'Error', roleSerializers.errors)
            return Response(response, status=code)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

class RolesDestroyView(DestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Roles.objects.get(id=pk)
        except Roles.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        role = self.get_object()
        if role is None:
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'Role Not Exist')
            return Response(response, status=code)
        if role.name.lower() == 'admin' or role.name.lower() == 'egresado':
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'No se puede borrar este rol')
            return Response(response, status=code)
        role.delete()

        response, code = create_response(
            status.HTTP_200_OK, 'Error', 'Ok')
        return Response(response, status=code)
