from  django import forms
from .models import Project, Achievement, Contact

class ProjectForm(forms.ModelForm):

    message = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Project
        fields =  [ 'message']


class AchievementForm(forms.ModelForm):

    message = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Achievement
        fields =  [ 'message']

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Phone'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Contact
        fields =  ['name', 'email', 'number', 'message']