from snacks.models import Snack
from django.urls import path
from .views import HomeView,SnackListView,SnackDetailView

urlpatterns = [
    # path('',HomeView.as_view(),name='home'),
    path('',SnackListView.as_view(),name='snack'),
    path('<int:pk>',SnackDetailView.as_view(),name='snackdetail')

]
