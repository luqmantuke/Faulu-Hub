from django.shortcuts import render
from blog.models import Post

def index(request):
    post = Post.objects.filter(status='Published')[0:6]
    context = {
        'post': post
    }
    return render(request, 'index-4.html', context)


def privacy(request):
    return render(request, 'privacy.html',)