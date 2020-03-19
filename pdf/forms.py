from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

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

            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "MIT"}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Bachelor"}),
            'edu_date_start': forms.DateInput(
                attrs={'class': 'form-control datepicker', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),
            'edu_date_end': forms.DateInput(
                attrs={'class': 'form-control datepicker', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),

            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position title'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Job description'}),
            'job_date_start': forms.DateInput(
                attrs={'class': 'form-control datepicker', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),
            'job_date_end': forms.DateInput(
                attrs={'class': 'form-control datepicker', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),

            'skills': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'C, C++, Python'}),
            'interests': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Sport, reading, music'}),
            'awards_and_certifications': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Write Google Analytics Certified Developer'}),
        }
