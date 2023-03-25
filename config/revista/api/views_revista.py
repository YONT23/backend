from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#from rest_framework.decorators import api_view


from ..models import *
from .permissions import *
from .serializers_revista import *

### Revisar
class RevisarCreateAV(generics.CreateAPIView):
    serializer_class = RevisarSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        usuario = Usuario.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Revisar.objects.filter(usuario=usuario, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie")
        
        if Revisar.number_rating == 0:
            Revisar.av_rating = serializer.validated_data['rating']
        else:
            Revisar.av_rating = (Revisar.av_rating + serializer.validated_data['rating'])/2
        
        Revisar.number_rating = Revisar.number_rating + 1
        Revisar.save()
        
        serializer.save(usuario=usuario, review_user=review_user)
        
class RevisarListAV(generics.ListAPIView):
    #queryset = Revisar.objects.all()
    serializer_class = RevisarSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Revisar.objects.filter(usuario=pk)  
    
class RevisarDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Revisar.objects.all()
    serializer_class = RevisarSerializer
    permission_classes = [RevisarUserOrReadOnly]

#class RevisarList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#    queryset = Revisar.objects.all()
#    serializer_class = RevisarSerializer
#    
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
#        
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)
#
#class RevisarDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#    queryset = Revisar.objects.all()
#    serializer_class = RevisarSerializer
#    
#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)

#### Tipo Usuario
     
class TipoUsuarioListAV(APIView):
    def get(self, request):
        tipousuario = TipoUsuario.objects.all()
        serializer = TipoUsuarioSerializers(tipousuario, many=True)
        permission_classes = [IsAuthenticated]
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        serializer = TipoUsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TipoUsuarioDetailsAV(APIView):
    def get(self, request, pk):
        try:
            persona = TipoUsuario.objects.get(pk=pk)
        except TipoUsuario.DoesNotExist:
            return Response({'Error': 'TipoUsuario not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoUsuarioSerializers(persona)  
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        persona = TipoUsuario.objects.get(pk=pk)
        serializer = TipoUsuarioSerializers(persona, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        persona = TipoUsuario.objects.get(pk=pk)
        persona.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

### Personas

class PersonaListAV(APIView):
    def get(self, request):
        personas = Personas.objects.all()
        serializer = PersonasSerializers(personas, many=True)
        permission_classes = [IsAuthenticated]
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        serializer = PersonasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PersonaDetailsAV(APIView):
    def get(self, request, pk):
        try:
            persona = Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            return Response({'Error': 'Personas not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonasSerializers(persona)  
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        persona = Personas.objects.get(pk=pk)
        serializer = PersonasSerializers(persona, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        persona = Personas.objects.get(pk=pk)
        persona.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

### Usuarios   
 
#class UsuarioPlataformVS(viewsets.ViewSet):
#    def list(self, request):
#        queryset = UsuarioPlataform.objects.all()
#        serializer = UsuarioPlataformSerializer(queryset, many=True)
#        return Response(serializers.data)
#    
#    def retrieve(self, request):
#        queryset = Revisar.objects.all()
#        usuario = get_object_or_404(queryset, pk=pk)
#        serializer = RevisarSerializer(usuario)
#        return Response(serializers.data)
    
class UsuarioListAV(APIView):
    
    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuariosSerializers(usuario, many=True, context={'request': request})
        permission_classes = [IsAuthenticated]
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UsuarioDetailsAV(APIView):
    def get(self, request, pk):
        try:
            persona = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({'Error': 'Usuario not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuariosSerializers(persona, context={'request': request})  
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        persona = Usuario.objects.get(pk=pk)
        serializer = UsuariosSerializers(persona, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        persona = Usuario.objects.get(pk=pk)
        persona.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

        