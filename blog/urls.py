from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.BlogPageList.as_view(), name='page_list'),
    path('blog/<slug:slug>/', views.detail, name='post_detail'),

]
