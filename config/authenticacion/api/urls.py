from django.urls import path, include

urlpatterns = [
    #path('auth/', include('authenticacion.api.view.auth.urls')),
    #path('users/', include('authenticacion.api.view.users.urls')),
    
    path('roles/', include('authenticacion.api.view.models_view.roles.urls')),
    path('resources/', include('authenticacion.api.view.models_view.resources.urls')),
    path('persons/', include('authenticacion.api.view.models_view.persons.urls')),
    path('genders/', include('authenticacion.api.view.models_view.gender.urls')),
    path('documents/', include('authenticacion.api.view.models_view.documents.urls')),
    path('security/',include('authenticacion.api.view.models_view.security.urls'))
]