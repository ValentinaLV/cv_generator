from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    linkedin_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    git_link = models.URLField(blank=True)

    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    edu_date_start = models.DateField()
    edu_date_end = models.DateField()

    position = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    job_date_start = models.DateField()
    job_date_end = models.DateField()

    skills = models.TextField(max_length=1000, blank=True)
    interests = models.TextField(max_length=1000, blank=True)
    awards_and_certifications = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CV Profile'
        verbose_name_plural = 'CV Profiles'
