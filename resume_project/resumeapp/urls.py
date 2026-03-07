from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_resume, name='create_resume'),
    path('resumes/',views.resume_list, name = 'resume_list'),
]