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


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler403(request, exception):
    return render(request, '403.html', status=403)


def handler400(request, exception):
    return render(request, '400.html', status=400)


def handler500(request):
    return render(request, '500.html', status=500)