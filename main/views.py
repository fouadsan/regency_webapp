from django.shortcuts import render
from .models import Project

def home(request):
    context = {
        'projects' : Project.objects.all(),
        'title': 'Home',
    }
    return render(request, 'main/index.html', context)
