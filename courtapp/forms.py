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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z ]+$', name):
            raise ValidationError('Name should contain only alphabets')
        return name

class JuryForm(forms.ModelForm):
    SPECIALIZATIONS = [
    ('Criminal', 'Criminal Law'),
    ('Civil', 'Civil Law'),
    ('Corporate', 'Corporate & Business Law'),
    ('Family', 'Family Law'),
    ('Intellectual Property', 'Intellectual Property (IP) Law'),
    ('Labor', 'Labor & Employment Law'),
    ('Tax', 'Taxation Law'),
    ('Immigration', 'Immigration Law'),
    ('Real Estate', 'Real Estate & Property Law'),
    ('Cyber', 'Cyber & Technology Law'),
    ('Environmental', 'Environmental Law'),
    ('Banking', 'Banking & Financial Law'),
    ('Human Rights', 'Human Rights & Constitutional Law'),
    ('Consumer', 'Consumer Protection Law'),
]
    specialization = forms.ChoiceField(choices=SPECIALIZATIONS, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Jury
        fields = ['name', 'email', 'phone', 'specialization']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'name': 'email'}),
            'phone': forms.TextInput(attrs={'id': 'phone', 'name': 'phone'}),
            'specialization': forms.TextInput(attrs={'id': 'specialization', 'name': 'specialization'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'specialization': 'Specialization',
        }
        help_texts = {
            'name': '',
            'email': '',
            'phone': '',
            'specialization': '',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z . ]+$', name):
            raise ValidationError('Name should contain only alphabets')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^[0-9]+$', phone):
            raise ValidationError('Phone should contain only numbers')
        return phone

    def clean_specialization(self):
        specialization = self.cleaned_data.get('specialization')
        if not re.match(r'^[a-zA-Z ]+$', specialization):
            raise ValidationError('Specialization should contain only alphabets')
        return specialization

class JuryUpdateForm(forms.ModelForm):
    SPECIALIZATIONS = [
    ('Criminal', 'Criminal Law'),
    ('Civil', 'Civil Law'),
    ('Corporate', 'Corporate & Business Law'),
    ('Family', 'Family Law'),
    ('Intellectual Property', 'Intellectual Property (IP) Law'),
    ('Labor', 'Labor & Employment Law'),
    ('Tax', 'Taxation Law'),
    ('Immigration', 'Immigration Law'),
    ('Real Estate', 'Real Estate & Property Law'),
    ('Cyber', 'Cyber & Technology Law'),
    ('Environmental', 'Environmental Law'),
    ('Banking', 'Banking & Financial Law'),
    ('Human Rights', 'Human Rights & Constitutional Law'),
    ('Consumer', 'Consumer Protection Law'),
]
    specialization = forms.ChoiceField(choices=SPECIALIZATIONS, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Jury
        fields = ['name', 'email', 'phone', 'specialization']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'name': 'email'}),
            'phone': forms.TextInput(attrs={'id': 'phone', 'name': 'phone'}),
            'specialization': forms.TextInput(attrs={'id': 'specialization', 'name': 'specialization'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'specialization': 'Specialization',
        }
        help_texts = {
            'name': '',
            'email': '',
            'phone': '',
            'specialization': '',
        }
        

class ScheduleTrial(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleTrial, self).__init__(*args, **kwargs)
        
        # Fetch Jury choices dynamically
        jury_choices = Jury.objects.all().values_list('id', 'name')
        
        # Set choices dynamically
        self.fields['jury'].queryset = Jury.objects.all()

    class Meta:
        model = Schedule
        fields = ['jury', 'scheduled_date', 'scheduled_time']
        widgets = {
            'jury': forms.Select(attrs={'class': 'form-control'}),
            'scheduled_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'scheduled_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
        labels = {
            'jury': 'Jury',
            'scheduled_date': 'Scheduled Date',
            'scheduled_time': 'Scheduled Time',
        }
        help_texts = {
            'jury': '',
            'scheduled_date': '',
            'scheduled_time': '',
        }

class RejectScheduleTrial(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['reject_reason']
        widgets = {
            'reject_reason': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'reject_reason': 'Reason for Rejection',
        }
        help_texts = {
            'reject_reason': '',
        }


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title', 'name': 'title'}),
            'description': forms.Textarea(attrs={'id': 'description', 'name': 'description'}),
            'file': ClearableFileInput(attrs={'id': 'file', 'name': 'file'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'file': 'File',
        }
        help_texts = {
            'title': '',
            'description': '',
            'file': '',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not re.match(r'^[a-zA-Z0-9 ]+$', title):
            raise ValidationError('Title should contain only alphabets and numbers')
        return title
        