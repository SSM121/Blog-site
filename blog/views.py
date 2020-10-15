from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.urls import reverse
from .models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect
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

def comment(request, blog_id):
    q = Comment(comment_author=request.POST['name'], comment_email=request.POST['email'],
            comment_content=request.POST['content'], comment_date=datetime.now(),
            blog=Post.objects.get(pk=blog_id))
    q.save()
    return HttpResponseRedirect(reverse('blog:single', args=(blog_id,)))
