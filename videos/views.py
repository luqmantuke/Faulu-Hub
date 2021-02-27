from django.shortcuts import render
from .models import Topic
from .filters import VideosFilter
from django.db.models import Q
from django.views.generic.list import ListView
from blog.models import Post
from books.models import Books


def videos_list(request):
    videos = Topic.objects.all().order_by('order')
    template_name = 'videos/videos_list.html'
    myFilter = VideosFilter(request.GET, queryset=videos)
    videos = myFilter.qs

    return render(request, template_name, {'content': videos,
                                           'myfilter': myFilter})


def videos_detail(request, slug):
    query = Topic.objects.filter(slug__iexact=slug)
    posts = Post.objects.filter(status='Published')[0:3]
    popular_books = Books.objects.filter(popular='Popular')[0:3]
    popular = Post.objects.filter(popular='Popular')[0:3]
    recent_books = Books.objects.all()[0:3]

    if query.exists():
        query = query.first()
    else:
        return render(request, '404.html', status=404)
    context = {
        'content': query,
        'posts': posts,
        'popular_books': popular_books,
        'popular': popular,
        'recent_books': recent_books,
    }

    return render(request, 'videos/video_detail.html', context)


class SearchResultsView(ListView):
    model = Topic
    template_name = 'videos/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Topic.objects.filter(
            Q(name__icontains=query) | Q(body__icontains=query)
        )

        return object_list