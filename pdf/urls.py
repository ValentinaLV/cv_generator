from django.urls import path

from .views import ProfileView
from .views import ResumeListView, ResumeView
from .views import GeneratePdf


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('resumes', ResumeListView.as_view(), name='resumes'),
    path('resume/<str:slug>', ResumeView.as_view(), name='resume-details'),
    path('download/<str:slug>', GeneratePdf.as_view(), name='resume-download'),

]

