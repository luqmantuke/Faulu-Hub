from django.urls import path
from . import views

urlpatterns = [
    path('video-list/', views.videos_list, name="videos_list"),
    path('video-list/<slug:slug>/', views.videos_detail, name='video_detail'),
    path('search/', views.SearchResultsView.as_view(), name='video_search_results'),
]
