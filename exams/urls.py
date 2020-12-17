from django.urls import path
from . import views

urlpatterns = [
    path('exams-list/', views.exam_list, name="exam_list"),
    path('exams-list/<slug:slug>/', views.exam_detail, name='exam_detail')
]
