from django.shortcuts import render
from .models import *

def home(request):
    context = {
        'projects' : Project.objects.all()[:6],
        'testimonials': Testimonial.objects.all(),
        'posts': Post.objects.all()[:2],
        'title': 'Home',
    }
    return render(request, 'main/index.html', context)
