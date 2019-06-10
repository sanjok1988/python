from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Post


# Create your views here.
def post_view(request, *args, **kwargs):   
    posts = Post.objects.get()
    context = {
        'posts':posts
    }
    return render(request, "posts.html", context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    context = {
        'post': post
    }
    return render(request, 'polls/detail.html', context)


def post_list_view(request, *args, **kwargs):
    context = {
        
    }
    return render(request, 'post_list.html', context)
