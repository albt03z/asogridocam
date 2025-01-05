from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ClientForm

# Create your views here.
class HomeView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ClientForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
