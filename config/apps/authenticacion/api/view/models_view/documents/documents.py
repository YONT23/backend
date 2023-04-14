from .....mudules import (ListAPIView, CreateAPIView, Response, status, UpdateAPIView, 
                          create_response, IsAdminRole, DestroyAPIView)
from apps.authenticacion.models import Document_types
from ....serializer.serializers import DocumentSerializers

class DocumentListView(ListAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = DocumentSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Document', serializers.data)
        return Response(response, status=code)

class DocumentCreateView(CreateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def post(self, request, *args, **kwargs):
        documentSerializers = DocumentSerializers(data=request.data)
        if documentSerializers.is_valid():
            documentSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Document', documentSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', documentSerializers.errors)
        return Response(response, status=code)

class DocumentUpdateView(UpdateAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers

    def get_object(self):

        try:
            pk = self.kwargs.get('pk')
            return Document_types.objects.get(pk=pk)
        except Document_types.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        document = self.get_object()

        if document is None:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', documentSerializers.errors)
            return Response(response, status=code)

        try:
            documentSerializers = DocumentSerializers(
                document, data=request.data)
            if documentSerializers.is_valid():
                documentSerializers.save()
                response, code = create_response(
                    status.HTTP_200_OK, 'Document Update', documentSerializers.data)
                return Response(response, status=code)
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', documentSerializers.errors)
            return Response(response, status=code)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

class DocumentDestroyView(DestroyAPIView):
    queryset = Document_types.objects.all()
    serializer_class = DocumentSerializers
    permission_classes = [IsAdminRole]

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            return Document_types.objects.get(id=pk)
        except Document_types.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        document = self.get_object()
        if document is None:
            response, code = create_response(
                status.HTTP_200_OK, 'Error', 'Type document Not Exist')
            return Response(response, status=code)
        document.delete()

        response, code = create_response(
            status.HTTP_200_OK, 'Error', 'Ok')
        return Response(response, status=code)