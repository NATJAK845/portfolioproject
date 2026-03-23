from django.shortcuts import render
from .models import Project  # import your Project model

def home(request):
    projects = Project.objects.all()  # fetch all projects
    return render(request, 'main/home.html', {
        'name': 'Nathaniel Zane Jakosalem',  # connects to {{ name }}
        'role': 'Web Designer',               # connects to {{ role }}
        'projects': projects                  # connects to {{ project }}
    })
