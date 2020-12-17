from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from .filters import NotesFilter


def content_list(request):
    notes = Content.objects.all()
    template_name = 'notes/content_list.html'
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    return render(request, template_name, {'content': notes,
        'myfilter': myFilter})

def content_detail(request, slug):
    q = Content.objects.filter(slug__iexact = slug)
    if q.exists(): 
        q = q.first()
    else: 
       return render(request, '404.html', status=404)
    
    context = {
        'content': q
    }

    return render(request, 'notes/content_detail.html', context)