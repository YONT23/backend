from django.urls import path, include
from .views import (LoginView, LogoutView, SignupView, ProfileView, 
                    UsersViewPublic, UserCreateView,  UserUpdateView, UserChangePasswordView)
urlpatterns = [
    # Auth views
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/signup/', SignupView.as_view(), name='auth_signup'),
    
    path('auth/reset/', include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
    
    #User
    path('user/profile/', ProfileView.as_view(), name='user_profile'),
    path('user/viewpublic/', UsersViewPublic.as_view(), name='user_viewpublic'),
    path('user/createview/', UserCreateView.as_view(), name='user_createview'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_createview'),
   
    path('<int:pk>/change/password/', UserChangePasswordView.as_view(), name='user_changepassword'),
    
]
