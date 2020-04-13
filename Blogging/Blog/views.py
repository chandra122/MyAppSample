from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Person1

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

personstext = [
    {
        'name' : 'sekhar',
        'shirt_size' : 'L'
    },
    {
        'name' : 'chandran',
        'shirt_size' : 'M'
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

def example(request):
    person = Person1.objects.create(name="Fred Flintstone", shirt_size="L")
    result = Person1.objects.all();
    print(result)

    context = {
        'persons' : result
    }
    return render(request,'Blog/about1.html',context)