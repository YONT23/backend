from django.urls import path, include

urlpatterns = [
    #path('auth/', include('authenticacion.api.view.auth.urls')),
    #path('users/', include('authenticacion.api.view.users.urls')),
    
    path('roles/', include('apps.authenticacion.api.view.models_view.roles.urls')),
    path('resources/', include('apps.authenticacion.api.view.models_view.resources.urls')),
    path('persons/', include('apps.authenticacion.api.view.models_view.persons.urls')),
    path('genders/', include('apps.authenticacion.api.view.models_view.gender.urls')),
    path('documents/', include('apps.authenticacion.api.view.models_view.documents.urls')),
    path('security/',include('apps.authenticacion.api.view.models_view.security.urls'))
]