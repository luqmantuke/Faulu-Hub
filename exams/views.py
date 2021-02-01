from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from .filters import ExamsFilter
from blog.models import Post
from books.models import Books

def exam_list(request):
    notes = ExamContent.objects.all()
    template_name = 'exams/exam_list.html'
    myFilter = ExamsFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    return render(request, template_name, {'content': notes,
        'myfilter': myFilter})


def exam_detail(request, slug):
    q = ExamContent.objects.filter(slug__iexact = slug)
    post = Post.objects.filter(status='Published')[0:3]
    popular_books = Books.objects.filter(popular='Popular')[0:3]
    popular = Post.objects.filter(popular='Popular')[0:3]
    recent_books = Books.objects.all()[0:3]

    if q.exists(): 
        q = q.first()
    else: 
       return render(request, '404.html', status=404)
    
    context = {
        'content': q,
        'post': post,
        'popular_books': popular_books,
        'popular': popular,
        'recent_books': recent_books,
    }

    return render(request, 'exams/exam_detail.html', context)