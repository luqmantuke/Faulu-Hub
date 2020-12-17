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



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/',  include('contact.urls')),
    path('notes/',  include('notes.urls')),
    path('exams/',  include('exams.urls')),
    path('course/', include('courses.urls')),
    path('', include('blog.urls')),
    path('forum/', include(machina_urls)),
    path('students/', include('students.urls')),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
]




handler403 = 'courses.views.handler403'
handler404 = 'courses.views.handler404'
handler400 = 'courses.views.handler400'
handler500 = 'courses.views.handler500'