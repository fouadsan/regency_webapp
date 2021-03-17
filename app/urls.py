from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blogs/', include('blog.urls')),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

