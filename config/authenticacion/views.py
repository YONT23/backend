from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django_rest_passwordreset.signals import reset_password_token_created

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView

from .serializers import UserSerializer, CreateUserSerializers, UserChangePassword
#from ...serializers.user.users_serializers import UserSerializers, CreateUserSerializers, UserChangePassword

from .models import CustomUser
from .mudules import create_response


class UsersViewPublic(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializers = UserSerializer(users, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'User Public', serializers.data)
        return Response(response, status=code)

class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializers

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def post(self, request, *args, **kwargs):
        userSerializers = self.get_serializer(data=request.data)
        if userSerializers.is_valid():
            self.perform_create(userSerializers)
            response, code = create_response(
                status.HTTP_200_OK, 'User Create', userSerializers.data)
            return Response(userSerializers.data, status=code)
        response, code = create_response(
            status.HTTP_200_OK, 'Error', userSerializers.data)
        return Response(response, status=code)

class UserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = CustomUser.objects.get(pk=request_user)
            return user
        except CustomUser.DoesNotExist:
            return None
        except Exception as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Error', e)
            return Response(response, status=code)

    def perform_update(self, serializer):
        serializer.save()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        if user is None:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password Error', 'User Not found')
            return Response(response, status=code)

        try:
            userSerializers = UserSerializer(
                user, data=request.data, partial=partial)
            if userSerializers.is_valid():
                self.perform_update(userSerializers)
                response, code = create_response(
                    status.HTTP_400_BAD_REQUEST, 'Password Error', 'User Not found')
                return Response(response, status=code)
            return Response(userSerializers.errors, 'Error', status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)
        
class UserChangePasswordView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            request_user = self.kwargs['pk']
            user = CustomUser.objects.get(pk=request_user)
            return user
        except (CustomUser.DoesNotExist, TypeError):
            return None
        except (BaseException, TypeError) as e:
            return None

    def perform_update(self, serializer):
        if 'original-password' in self.request.data:
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()

        if user is None:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

        if 'original-password' not in self.request.data:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password Error', 'Password not found')
            return Response(response, status=code)

        if not user.check_password(request.data['original-password']):
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Password Error', 'Password is not correct.')
            return Response(response, status=code)

        userSerializers = UserChangePassword(
            user, data=request.data, partial=partial, context={'context': request})

        try:
            if userSerializers.is_valid():
                self.perform_update(userSerializers)
                response, code = create_response(
                    status.HTTP_200_OK, 'Password', 'Password Change')
                return Response(response, status=code)
            return Response(userSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            response, code = create_response(
                status.HTTP_400_BAD_REQUEST, 'Not Found', e.args)
            return Response(response, status=code)

class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(UserSerializer(user).data,status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Aquí deberíamos mandar un correo al cliente...
    print(f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/.")
