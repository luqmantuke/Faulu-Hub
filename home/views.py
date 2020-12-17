from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('-publish')[0:6]
    context = {
        'post': posts
    }

    return render(request, 'index-4.html', context)

