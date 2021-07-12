from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DeleteView
from .models import Snack

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DeleteView):
    template_name = 'snack_detail.html'
    model = Snack