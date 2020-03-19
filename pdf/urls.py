from django.urls import path

from .views import ProfileView, ResumeListView, ResumeView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('resumes', ResumeListView.as_view(), name='resumes'),
    path('resume/<str:slug>', ResumeView.as_view(), name='resume-details'),

]

