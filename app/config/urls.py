"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

from mail.views import send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search_flight.urls')),
    path('mail/', include('mail.urls')),
]
=======
from django.urls import path, re_path, include

from config import settings
from config.views import serve_media
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ticket/', include('ticket.urls')),
    # re_path(r'media/(?P<path>.*)$', serve_media),
]+ static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
>>>>>>> master
