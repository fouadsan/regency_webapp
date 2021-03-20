from django.urls import path
from .views import home, about, services, service_detail, projects, project_details


app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('services/<int:_id>', service_detail, name='service_detail'),
    path('projects', projects, name='projects'),
    path('projects/<int:_id>', project_details, name='project'),

]
