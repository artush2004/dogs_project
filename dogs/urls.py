from django.urls import path
from .views import (DogListView,
                    DogDetailView,
                    DogCreateView,
                    DogDeleteView,)

urlpatterns = [
    path('dog/<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete'),
    path('dog/new/', DogCreateView.as_view(), name='dog_new'),
    path('dog/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('', DogListView.as_view(), name='home'),
]
