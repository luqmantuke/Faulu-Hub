import django_filters
from .models import *


class NotesFilter(django_filters.FilterSet):
    class Meta:
        model = Content
        fields = '__all__'
        exclude = ['name', 'slug', 'body', 'image', 'order', 'created']
