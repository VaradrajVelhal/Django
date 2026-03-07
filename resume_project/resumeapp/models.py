from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()

    # New Fields
    projects = models.TextField(default='', blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.full_name