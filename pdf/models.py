from time import time
from datetime import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def get_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    linkedin_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    git_link = models.URLField(blank=True)
    skills = models.TextField(max_length=1000, blank=True)

    experience = models.TextField()
    education = models.TextField(max_length=2000)

    interests = models.TextField(max_length=1000, blank=True)
    awards_and_certifications = models.TextField(max_length=2000, blank=True)

    url = models.SlugField(max_length=200, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url = get_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pdf:resume-details', kwargs={'slug': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CV Profile'
        verbose_name_plural = 'CV Profiles'
        ordering = ['-created']
