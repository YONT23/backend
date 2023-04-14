from ....serializer.serializers import PersonsSerializers
from apps.authenticacion.models import Persons
from rest_framework import status
from .....mudules import ListAPIView, CreateAPIView, UpdateAPIView, Response, create_response


class PersonView(ListAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = PersonsSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Person', serializers.data)
        return Response(response, status=code)


class PersonCreateView(CreateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def post(self, request, *args, **kwargs):
        personSerializers = PersonsSerializers(data=request.data)
        if personSerializers.is_valid():
            personSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Person', personSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', personSerializers.errors)
        return Response(response, status=code)


class PersonUpdateView(UpdateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def get_object(self):
        try:
            pk = self.request.user.id
            return Persons.objects.filter(user__id=pk)[0]
        except Persons.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        person = self.get_object()
        if person is None:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', personSerializers.data)
            return Response(response, status=code)
        try:
            personSerializers = PersonsSerializers(person, data=request.data)
            if personSerializers.is_valid():
                personSerializers.update()
                response, code = create_response(
                    status.HTTP_200_OK, 'Person Update', personSerializers.data)
                return Response(response, status=code)
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', personSerializers.data)
            return Response(response, status=code)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)
