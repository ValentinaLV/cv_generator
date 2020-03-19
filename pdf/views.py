from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Profile
from .forms import ProfileForm


class ProfileView(View):
    def get(self, request):
        profile_form = ProfileForm()
        return render(request, 'base.html', {
            'form': profile_form
        })

    def post(self, request):
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            messages.success(request, "Your CV was successfully created)")
            profile_form.save()
            return redirect('pdf:resumes')
        else:
            messages.error(request, "Your CV wasn't created...")


class ResumeListView(View):
    def get(self, request):
        resumes = Profile.objects.all()
        return render(request, 'resume_list.html', {
            'resumes': resumes
        })


class ResumeView(View):
    def get(self, request, slug):
        resume = Profile.objects.get(url=slug)
        return render(request, 'resume.html', {
            'resume': resume
        })
