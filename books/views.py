from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.conf import settings
from FAULU_HUB import settings
from .models import Books
from blog.models import Post
from .filters import BooksFilter



def books_list(request):
    books = Books.objects.all()
    template_name = 'books/books_list.html'
    myFilter = BooksFilter(request.GET, queryset=books)
    books = myFilter.qs

    return render(request, template_name, {'books': books,
        'myfilter': myFilter})




def book_detail(request, slug):
    q = Books.objects.filter(slug__iexact=slug)
    posts = Post.objects.filter(status='Published')[0:3]
    popular_books = Books.objects.filter(popular='Popular')[0:3]
    popular = Post.objects.filter(popular='Popular')[0:3]
    recent_books = Books.objects.all()[0:3]

    if q.exists():
        q = q.first()
    else:
        return render(request, '404.html', status=404)

    context = {
        'book': q,
        'posts': posts,
        'popular_books': popular_books,
        'popular': popular,
        'recent_books': recent_books,
    }
    return render(request, 'books/book_detail.html', context)


