import django_filters
from .models import *


class ExamsFilter(django_filters.FilterSet):
    class Meta:
        model = Content
        fields = '__all__'
        exclude = ['name', 'slug', 'body', 'image', 'subject', 'form']