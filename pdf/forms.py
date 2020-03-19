from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
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

            'skills': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'C, C++, Python'}),

            'experience': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Type company name, job description and dates of beginning and end of job'}),

            'education': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Type university, degree and dates of beginning and end of study'}),

            'interests': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Sport, reading, music'}),
            'awards_and_certifications': forms.Textarea(
                attrs={'class': 'form-control', 'cols': "100", 'rows': "10",
                       'placeholder': 'Write Google Analytics Certified Developer'}),
        }
