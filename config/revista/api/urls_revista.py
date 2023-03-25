from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_revista import *

router = DefaultRouter()
#router.register('user', UsuarioPlataformVS.as_view(), basename='user-plataform')

urlpatterns = [
    #Personas
    path('perslist/', PersonaListAV.as_view(), name='peron-list'),
    path('perslist/<int:pk>/', PersonaDetailsAV.as_view(), name='peron-details'),
    
    #Tipo Usuario
    path('tpuserlist/', TipoUsuarioListAV.as_view(), name='tpuser-list'),
    path('tpuserlist/<int:pk>/', TipoUsuarioDetailsAV.as_view(), name='tpuser-details'),

    #Usuario
    #path('', include(router.urls)),
    path('userlist/', UsuarioListAV.as_view(), name='user-list'),
    path('userlist/<int:pk>/', UsuarioDetailsAV.as_view(), name='user-details'),
    
    #Revisar
    #path('revisar/', RevisarListAV.as_view(), name='revisar-list'),
    #path('revisar/<int:pk>/', RevisarDetailAV.as_view(), name='revisar-details'),
    path('userlist/<int:pk>/revisar-create/', RevisarCreateAV.as_view(), name='revisar-create'),
    path('userlist/<int:pk>/revisar/', RevisarListAV.as_view(), name='revisar-list'),
    path('userlist/revisar/<int:pk>/', RevisarDetailAV.as_view(), name='revisar-details'),
]