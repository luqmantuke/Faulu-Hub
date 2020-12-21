from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from .filters import NotesFilter
from django.db.models import Q


def content_list(request):
    notes = Content.objects.all().order_by('order')
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


class SearchResultsView(ListView):
    model = Content
    template_name = 'notes/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Content.objects.filter(
            Q(name__icontains=query) | Q(body__icontains=query)
        )
        return object_list