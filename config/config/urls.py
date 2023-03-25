
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('revista/', include('revista.api.urls_revista')),
    path('account/', include('user_app.api.url_user')),
    #path('api-auth/', include('rest_framework.urls')),
]
