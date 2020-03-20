from django import forms
from pagedown.widgets import PagedownWidget

from .models import Profile


class ProfileForm(forms.ModelForm):
    skills = forms.CharField(widget=PagedownWidget)
    experience = forms.CharField(widget=PagedownWidget)
    education = forms.CharField(widget=PagedownWidget)
    interests = forms.CharField(widget=PagedownWidget)
    awards_and_certifications = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Profile
        exclude = ('url',)

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'John Doe', 'required': 'required'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'style': "margin-top: 15px;", 'placeholder': 'demo@gmail.com'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'style': "margin-top: 15px;", 'placeholder': '+38 099 170 7777'}),
            'summary': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Write something about you'}),
            'linkedin_link': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'https://www.linkedin.com/in/valentyna-lysenok/',
                       'required': 'required'}),
            'git_link': forms.TextInput(
                attrs={'class': 'form-control', 'style': "margin-top: 15px;",
                       'placeholder': 'https://github.com/ValentinaLV'}),
            'facebook_link': forms.TextInput(
                attrs={'class': 'form-control', 'style': "margin-top: 15px;",
                       'placeholder': 'https://www.facebook.com/tinalysenok'}),

        }
