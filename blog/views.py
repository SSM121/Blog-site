from django.shortcuts import render
from datetime import datetime

def about(request):
    now = datetime.now()
    context = {'time': now, }
    return render(request, 'blog/about.html', context)

def tips(request):
    now = datetime.now()
    context = {'time': now, }
    return render(request, 'blog/tips.html', context)
