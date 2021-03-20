from django.http import Http404
from django.shortcuts import render
from .models import *
from blog.models import BlogModel
from contact.models import Contact
# import mailchimp_marketing as mail_market
# from mailchimp_marketing.api_client import ApiClientError
# from app.settings import mailchimp_api_key, mailchimp_server, mailchimp_list_id
# from .forms import EmailSignupForm
from django.contrib import messages


# mailchimp = mail_market.Client()
# mailchimp.set_config({
#     "api_key": mailchimp_api_key,
#     "server": mailchimp_server
# })
#
# list_id = mailchimp_list_id
#
#
# def subscribe(email):
#     member_info = {
#         "email_address": email,
#         "status": "subscribed",
#     }
#
#     try:
#         mailchimp.lists.add_list_member(list_id, member_info)
#     except ApiClientError as error:
#         print("An exception occurred: {}".format(error.text))
#

def home(request):
    sections = Section.objects.all()
    abouts = About.objects.all()[:1]
    projects = Project.objects.all()[:6]
    teams = Team.objects.all()[:4]
    contacts = Contact.objects.all()[:1]
    counters = ProjectCounter.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    blogs = BlogModel.objects.all()[:2]
    # form_subscribe = EmailSignupForm()
    # if request.method == "POST" and "subscribe" in request.POST:
    #     form_subscribe = EmailSignupForm(request.POST)
    #     email = str(form_subscribe['email'].value())
    #     if form_subscribe.is_valid():
    #         email_signup_queryset = Signup.objects.filter(email=email)
    #         if email_signup_queryset.exists():
    #             messages.info(request, "You are already subscribed")
    #         else:
    #             subscribe(email)
    #             form_subscribe.save()
    #             messages.success(request, "You are now subscribed")
    context = {
        'sections': sections,
        'abouts': abouts,
        'projects': projects,
        'teams': teams,
        'contacts': contacts,
        'counters': counters,
        'testimonials': testimonials,
        'blogs': blogs,
        # 'form_subscribe': form_subscribe
    }
    return render(request, 'main/index.html', context)


def about(request):
    abouts = About.objects.all()[:1]
    teams = Team.objects.all()
    context = {
        'title': 'About Us',
        'abouts': abouts,
        'teams': teams,
    }

    return render(request, 'main/about.html', context)


def services(request):
    sections = Section.objects.all()
    context = {
        'title': 'Services',
        'sections': sections
    }
    return render(request, 'main/services.html', context)


def service_detail(request, _id):
    try:
        sections = Section.objects.all()
        data = Section.objects.get(id=_id)
    except Section.DoesNotExist:
        raise Http404('Data does not exist')

    context = {
        'title': 'Service Detail',
        'sections': sections,
        'data': data,
    }
    return render(request, 'main/service_detail.html', context)


def projects(request):
    sections = Section.objects.all()
    projects = Project.objects.all()
    context = {
        'title': 'Projects',
        'sections': sections,
        'projects': projects
    }
    return render(request, 'main/projects.html', context)


def project_details(request, _id):
    try:
        sections = Section.objects.all()
        data = Project.objects.get(id=_id)
    except Project.DoesNotExist:
        raise Http404('Data does not exist')

    context = {
        'title': 'Project Details',
        'sections': sections,
        'data': data,
    }
    return render(request, 'main/project_details.html', context)