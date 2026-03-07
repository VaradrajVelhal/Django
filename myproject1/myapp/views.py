from django.shortcuts import render

def home(request):
    context = {
        'name': 'Varadraj Velhal',
        'course': 'MCA Semester 2',
        'college': 'Pimpri Chinchwad College of Engineering',
    }
    return render(request, 'myapp/home.html', context)