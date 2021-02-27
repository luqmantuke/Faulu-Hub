import django_filters
from .models import *


class VideosFilter(django_filters.FilterSet):
    class Meta:
        model = Topic
        fields = ['form', 'subject']

