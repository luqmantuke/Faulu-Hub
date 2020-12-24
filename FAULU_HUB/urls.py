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
from django.contrib.auth import views as auth_views
from courses.views import CourseListView
from machina import urls as machina_urls
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post
from notes.models import Content
from exams.models import ExamContent
from django.views.generic import TemplateView

notes_dict = {
    'queryset': Content.objects.all(),
    'date_field': 'created'
}

exams_dict = {
    'queryset': ExamContent.objects.all(),
    'date_field': 'created'
}

blog_dict = {
    'queryset': Post.objects.filter(status='Published'),
    'date_field': 'created'
}

sitemaps = {
    'notes': GenericSitemap(notes_dict, priority=0.6),
    'exams': GenericSitemap(exams_dict, priority=0.6),
    'blog': GenericSitemap(blog_dict, priority=0.6),
}

urlpatterns = [
    path('vaultadmins/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/',  include('contact.urls')),
    path('notes/',  include('notes.urls')),
    path('exams/',  include('exams.urls')),
    path('course/', include('courses.urls')),
    path('', include('blog.urls')),
    path('forum/', include(machina_urls)),
    path('students/', include('students.urls')),
    path('accounts/', include('allauth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]




handler403 = 'courses.views.handler403'
handler404 = 'courses.views.handler404'
handler400 = 'courses.views.handler400'
handler500 = 'courses.views.handler500'