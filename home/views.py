from django.shortcuts import render


def index(request):

    return render(request, 'index-4.html')


def privacy(request):
    return render(request, 'privacy.html',)