from typing import Any
from django import forms

from pages.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'reason', 'message']
        error_messages = {
            'name': {
                'required': 'Le nom est obligatoire.',
            },
            'email': {
                'required': 'Fournissez un email valide.',
            },
            'reason': {
                'required': 'Donnez la raison de votre message.',
            },
            'message': {
                'required': 'Le message est obligatoire..',
            }

        }
            
    def clean_message(self):
        cleaned_data = super().clean()
        message = cleaned_data.get('message')
        if message and len(message) < 10:
            raise forms.ValidationError('Votre message est assez court')
        return message
