from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.conf import settings
from FAULU_HUB import settings
from .models import Post
from books.models import Books

class BlogPageList(ListView):
  model = Post
  template_name = 'blog/page_list.html'
  paginate_by = 12
  context_object_name = 'posts'

  def get_queryset(self, *args, **kwargs):
    if self.kwargs:
      return Post.objects.filter(status='published').order_by('-created')
    else:
      query = Post.objects.filter(status='Published').order_by('-created')
      return query

def detail(request, slug):
    q = Post.objects.filter(slug__iexact = slug)
    posts = Post.objects.filter(status='Published')[0:3]
    popular_books = Books.objects.filter(popular='Popular')[0:3]
    popular = Post.objects.filter(popular='Popular')[0:3]
    recent_books = Books.objects.all()[0:3]

    if q.exists(): 
        q = q.first()
    else: 
       return render(request, '404.html', status=404)
  
    context = {
        'post': q,
        'posts': posts,
         'popular_books': popular_books,
        'popular': popular,
        'recent_books': recent_books,
        }
    return render(request, 'blog/post_detail.html', context) 
