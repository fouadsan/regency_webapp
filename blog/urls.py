from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogListView, name='blogs'),
    path('<int:_id>', BlogDetailView, name='blog'),
]