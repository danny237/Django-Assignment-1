from django.shortcuts import render
from . models import Posts
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'posts/home.html', {'title': 'Home'})


def blog_list(request):
    posts       = Posts.objects.all()
    context     = {
        'posts': posts,
        'title': 'List'
    }
    return render(request, 'posts/blog_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    context = {
        'post': post
    }

    return render(request, 'posts/detail.html', context)
