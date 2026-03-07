from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
# Create your views here.
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'create_resume.html',{'form':form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})