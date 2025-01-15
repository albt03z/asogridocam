from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ClientForm, SubscriberForm

class HomeView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ClientForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscriber_form'] = SubscriberForm()
        return context

    def post(self, request, *args, **kwargs):
        # Determinar qué formulario se envió
        if 'subscribe' in request.POST:
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                messages.success(request, '¡Gracias por suscribirte!')
                return redirect('home')
            else:
                messages.error(request, 'Este correo ya está registrado o es inválido.')
                return redirect('home')
        else:
            # Procesar el formulario de contacto
            return super().post(request, *args, **kwargs)