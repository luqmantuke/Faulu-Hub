import django_filters
from .models import *


class BooksFilter(django_filters.FilterSet):
    class Meta:
        model = Books
        fields = ['level']