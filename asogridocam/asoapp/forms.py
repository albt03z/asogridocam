from django import forms
from .models import Clients

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

