from .....mudules import path
from .roles import RolescreateView, RolesListView, RoleUpdateView, RolesDestroyView

urlpatterns = [
    path('', RolesListView.as_view()),
    path('update/<int:pk>', RoleUpdateView.as_view()),
    path('create/', RolescreateView.as_view()),
    path('delete/<int:pk>', RolesDestroyView.as_view()),
]
