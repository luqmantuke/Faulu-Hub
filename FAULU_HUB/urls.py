"""FAULU_HUB URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from machina import urls as machina_urls


from django.views.generic import TemplateView

urlpatterns = [
    path('vaultadmins/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/',  include('contact.urls')),
    path('notes/',  include('notes.urls')),
    path('exams/',  include('exams.urls')),
    path('videos/',  include('videos.urls')),
    path('', include('blog.urls')),
    path('', include('books.urls')),
    path('forum/', include(machina_urls)),


    path('accounts/', include('allauth.urls')),

    path("sitemap.xml/", TemplateView.as_view(template_name="sitemap.xml"),),
    path('ads.txt/', TemplateView.as_view(template_name="ads.txt", content_type="text/plain"),),
]




handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'
handler400 = 'home.views.handler400'
handler500 = 'home.views.handler500'