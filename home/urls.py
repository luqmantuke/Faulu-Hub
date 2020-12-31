from django.urls import path
from .views import index, privacy


urlpatterns = [
    path('', index, name="home"),
    path('privacy/', privacy, name="privacy")
]
