from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author' : 'chandra Sekhar',
        'title' : 'Blog Post 1',
        'content' : 'First Post',
        'date_published' : 'April 08 2020'
    },
    {
        'author' : 'Revenger',
        'title' : 'Blog Post 2',
        'content' : 'Second Post',
        'date_published' : 'April 08 2020'
    },
]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'Blog/home.html',context)

def about(request):
    context = {
        'posts':posts
    }
    return render(request,'Blog/about.html',context)
