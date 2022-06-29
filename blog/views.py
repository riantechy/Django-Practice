from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Chirchir',
        'title': 'first Blog',
        'content': 'my first content',
        'date_posted': 'July 27, 2022'
    },
    {
        'author': 'Chirchir',
        'title': 'first Blog',
        'content': 'my first content',
        'date_posted': 'July 27, 2022'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)

def about(request):
    return render (request, 'blog/about.html', {'title': 'about'})

# Create your views here.
