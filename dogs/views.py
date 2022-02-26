from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Dog

class DogListView(ListView):
    model = Dog
    template_name = 'home.html'

class DogDetailView(DetailView):
    model = Dog
    template_name = 'dog_detail.html'

class DogCreateView(CreateView):
    model = Dog
    template_name = 'dog_new.html'
    fields = ['name', 'author', 'age']

class DogDeleteView(DeleteView):
    model = Dog
    template_name = 'dog_delete.html'
    success_url = reverse_lazy('home')
