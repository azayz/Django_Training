from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'Author' : 'Aziz',
        'Title' : 'Somewhere in the dark',
        'Content' : 'Lies a mistery',
        'Date' : '13 November 2020' 
    },
    {
        'Author' : 'Aziz2',
        'Title' : 'Somewhere in the dark',
        'Content' : 'Lies a mistery',
        'Date' : '15 November 2020' 
    }    
]

def home(request) :

    context = {
        'posts' : posts
    }

    return render(request,'blog/home.html',context=context)

def about(request) :
    return render(request,'blog/about.html',{'title' : 'About'})  