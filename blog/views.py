from cgitb import html
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    ) 
from multiprocessing import context
from django.shortcuts import render
from requests import post
from sqlalchemy import false, true
from .models import Post



def index(request):
    
    return render (request, 'blog/index.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)

# listing the posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    #ordering the posts from the newest to the oldest
    ordering = ('-date_posted') 

# Creating the list of each post
class PostDetailView(DetailView):
    model = Post

# Creating the list of each post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
  
#   getting the author of the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update the list of each post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
  
#   getting the author of the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# function to test if the user is the author of the post before updating
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return true
        return false

# Deleating the list of each post
class PostDeleteView(DeleteView):
    model = Post

#link to redirect the user to detail view page after deleting.
    success_url= ('/') 

#function to test if the user is the author of the post before deleting
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return true
        return false

def about(request):
    return render (request, 'blog/about.html', {'title': 'about'})

# Create your views here.
