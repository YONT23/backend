from .....mudules import path
from .resources import  ResourcesListView, ResourcesUpdateView,ResourcesDestroyView

urlpatterns = [
    path('roles/', ResourcesListView.as_view()),
    path('update/<int:pk>', ResourcesUpdateView.as_view()),
    path('delete/<int:pk>', ResourcesDestroyView.as_view()),
]
