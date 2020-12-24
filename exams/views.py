from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from .filters import ExamsFilter


def exam_list(request):
    notes = ExamContent.objects.all()
    template_name = 'exams/exam_list.html'
    myFilter = ExamsFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    return render(request, template_name, {'content': notes,
        'myfilter': myFilter})

def exam_detail(request, slug):
    q = ExamContent.objects.filter(slug__iexact = slug)
    if q.exists(): 
        q = q.first()
    else: 
       return render(request, '404.html', status=404)
    
    context = {
        'content': q
    }

    return render(request, 'exams/exam_detail.html', context)