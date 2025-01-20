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
        context['form'] = ClientForm()  # Para el formulario de contacto
        context['subscriber_form'] = SubscriberForm()  # Para el formulario de suscripción
        return context

    def post(self, request, *args, **kwargs):
        # Determinar qué formulario se envió
        if 'subscribe' in request.POST:
            # Procesar formulario de suscripción
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                messages.success(request, '¡Gracias por suscribirte!')
                return redirect('home')
            else:
                messages.error(request, 'Este correo ya está registrado o es inválido.')
                return redirect('home')
        else:
            # Procesar formulario de contacto
            contact_form = ClientForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, '¡Mensaje enviado correctamente!')
                return redirect('home')
            else:
                # Si hay errores, volver a mostrar el formulario con los errores
                return render(request, self.template_name, {
                    'form': contact_form,
                    'subscriber_form': SubscriberForm()
                })

class AboutView(TemplateView):
    template_name = 'aboutus.html'