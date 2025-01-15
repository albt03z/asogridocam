from django import forms
from .models import Clients, Subscriber
import re

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'surname', 'email', 'phone_number', 'country', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre', 'required': True}),
            'surname': forms.TextInput(attrs={'placeholder': 'Apellidos', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo Electrónico', 'required': True}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Teléfono', 'required': True}),
            'country': forms.Select(attrs={'placeholder': 'País de residencia', 'class': 'country-area nice-select', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Tu Mensaje', 'required': True}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError('El nombre solo puede contener letras.')
        return name
    
    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if not surname.isalpha():
            raise forms.ValidationError('El apellido solo puede contener letras.')
        return surname
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Clients.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        if not '@' in email:
            raise forms.ValidationError('El correo electrónico debe contener un "@".')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise forms.ValidationError('Por favor, ingrese un correo válido.')
        if len(email) > 30:
            raise forms.ValidationError('El correo electrónico no puede tener más de 100 caracteres.')
        if not email.endswith('.com') and not email.endswith('.es'):
            raise forms.ValidationError('El correo electrónico debe terminar en .com o .es')
        if not 'gmail' in email and not 'hotmail' in email and not 'yahoo' in email and not 'outlook' in email:
            raise forms.ValidationError('Solo se permiten correos de Gmail, Hotmail y Yahoo.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError('El número de teléfono solo puede contener números.')
        if len(phone_number) != 10:
            raise forms.ValidationError('El número de teléfono debe tener 10 dígitos.')
        return phone_number
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10  or len(message) > 400:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return message

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Tu correo electrónico',
                'class': 'footer-input',
                'required': True,
            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        if not '@' in email:
            raise forms.ValidationError('El correo electrónico debe contener un "@".')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise forms.ValidationError('Por favor, ingrese un correo válido.')
        return email