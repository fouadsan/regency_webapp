from django.shortcuts import render
from .models import *
from blog.models import BlogModel

def home(request):
    projects = Project.objects.all()[:6]
    counters = ProjectCounter.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    blogs = BlogModel.objects.all()[:2]
    context = {
        'projects' : projects,
        'counters': counters,
        'testimonials': testimonials,
        'blogs': blogs,
    }
    return render(request, 'main/index.html', context)
