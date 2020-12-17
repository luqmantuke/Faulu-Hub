from django.urls import path
from . import views

urlpatterns = [
    path('notes-list/', views.content_list, name="content_list"),
    path('notes-list/<slug:slug>/', views.content_detail, name='content_detail')
]
