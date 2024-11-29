from django.shortcuts import render
from .models import Cafe
from .forms import UserInput
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = 'source/home.html'


class CafeList(ListView):
    model = Cafe
    context_object_name = 'cafe'
    fields = "__all__"
    template_name = 'source/allcafes.html'


class AddCafe(CreateView):
    model= Cafe
    form_class = UserInput
    context_object_name = 'cafe'
    template_name = 'source/add.html'
    success_url = reverse_lazy("cafe")

    def form_valid(self,form):
        return super().form_valid(form)



