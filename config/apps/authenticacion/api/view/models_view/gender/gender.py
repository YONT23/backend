from .....mudules import (CreateAPIView, ListAPIView, UpdateAPIView, status, 
                          Response, create_response,IsAdminRole,DestroyAPIView)
from apps.authenticacion.models import Genders
from ....serializer.serializers import GenderSerializers


class GenderListView(ListAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = GenderSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Genders', serializers.data)
        return Response(response, status=code)


class GenderCreateView(CreateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def post(self, request, *args, **kwargs):
        genderSerializers = GenderSerializers(data=request.data)
        if genderSerializers.is_valid():
            genderSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Genders', genderSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', genderSerializers.errors)
        return Response(response, status=code)


class GenderUpdateView(UpdateAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Genders.objects.get(pk=pk)
        except Genders.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        gender = self.get_object()

        if gender is None:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', 'Gender Not Found')
            return Response(response, status=code)

        try:
            genderSerializers = GenderSerializers(gender, data=request.data)
            if genderSerializers.is_valid():
                genderSerializers.update(
                    gender, genderSerializers.validated_data)
                response, code = create_response(
                    status.HTTP_200_OK, 'Gender Update', genderSerializers.data)
                return Response(response, status=code)
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', genderSerializers.errors)
            return Response(response, status=code)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

class GendersDestroyView(DestroyAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Genders.objects.get(id=pk)
        except Genders.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        gender = self.get_object()
        if gender is None:
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'Gender Not Exist')
            return Response(response, status=code)
        gender.delete()

        response, code = create_response(
            status.HTTP_200_OK, 'Error', 'Ok')
        return Response(response, status=code)