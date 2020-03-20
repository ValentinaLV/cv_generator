import io

import pdfkit
from django.contrib import messages
from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.base import View
from reportlab.pdfgen import canvas

from .forms import ProfileForm
from .models import Profile
from .utils import Render


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


def resume(request, slug):
    user_profile = Profile.objects.get(url=slug)
    template = loader.get_template('resume.html')
    html = template.render({'resume': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response


def some_view(request, slug):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, f"Hello world. + {slug}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class GeneratePdf(View):
    def get(self, request, slug):
        user_profile = Profile.objects.get(url=slug)
        params = {
            'resume': user_profile,
            'request': request
        }
        return Render.render('resume.html', params)
