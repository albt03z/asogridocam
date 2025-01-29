from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ClientForm, SubscriberForm
from .models import Ally

class HomeView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ClientForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ClientForm()
        context['subscriber_form'] = SubscriberForm()
        return context

    def post(self, request, *args, **kwargs):
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
            contact_form = ClientForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, '¡Mensaje enviado correctamente!')
                return redirect('home')
            else:
                return render(request, self.template_name, {
                    'form': contact_form,
                    'subscriber_form': SubscriberForm()
                })

class AboutView(TemplateView):
    template_name = 'aboutus.html'
    form_class = SubscriberForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscriber_form'] = SubscriberForm()
        context['allies'] = Ally.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
            messages.success(request, '¡Gracias por suscribirte!')
            return redirect('about')
        else:
            messages.error(request, 'Este correo ya está registrado o es inválido.')
            return redirect('about')

class ContactView(TemplateView):
    template_name = 'contactus.html'
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ClientForm()
        context['subscriber_form'] = SubscriberForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'subscribe' in request.POST:
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                messages.success(request, '¡Gracias por suscribirte!')
                return redirect('contact')
            else:
                messages.error(request, 'Este correo ya está registrado o es inválido.')
                return redirect('contact')
        else:
            contact_form = ClientForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, '¡Mensaje enviado correctamente!')
                return redirect('contact')
            else:
                return render(request, self.template_name, {
                    'form': contact_form,
                    'subscriber_form': SubscriberForm()
                })