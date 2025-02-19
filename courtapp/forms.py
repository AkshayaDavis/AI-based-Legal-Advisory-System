from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from django.forms import ClearableFileInput


class LawForm(forms.ModelForm):
    class Meta:
        model = Law
        fields = ['name', 'ipc', 'description', 'year_of_act']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'name': 'name'}),
            'ipc': forms.TextInput(attrs={'id': 'ipc', 'name': 'ipc'}),
            'description': forms.Textarea(attrs={'id': 'description', 'name': 'description'}),
            'year_of_act': forms.DateInput(attrs={'id': 'year_of_act', 'name': 'year_of_act', 'type': 'date'}),
        }
        labels = {
            'name': 'Name',
            'ipc': 'IPC Section',
            'description': 'Description',
            'year_of_act': 'Year of Act',
        }
        help_texts = {
            'name': '',
            'ipc': '',
            'description': '',
            'year_of_act': '',
        }