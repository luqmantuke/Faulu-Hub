import django_filters
from .models import *


class VideosFilter(django_filters.FilterSet):
    class Meta:
        model = Topic
        fields = '__all__'
        exclude = ['name', 'slug', 'body', 'image', 'order', 'created', 'video']

