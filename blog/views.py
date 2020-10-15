from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Post, Comment
def about(request):
    now = datetime.now()
    context = {'time': now, }
    return render(request, 'blog/about.html', context)

def tips(request):
    now = datetime.now()
    context = {'time': now, }
    return render(request, 'blog/tips.html', context)

def home(request):
    latest_post = Post.objects.order_by('-blog_date')[:3]
    context = {'latest_post_list': latest_post,}
    return render(request, 'blog/index.html', context)

def archive(request):
    latest_post = Post.objects.order_by('-blog_date')
    context = {'latest_post_list': latest_post,}
    return render(request, 'blog/archive.html', context)


def single(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)

    return render(request, 'blog/single.html', {'post': post})
