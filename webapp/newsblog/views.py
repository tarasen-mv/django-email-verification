from django.shortcuts import render
from django.template import loader

from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('newsblog/index.html')
    context = {
        'posts_list': posts,
    }
    return render(request, 'newsblog/index.html', context)
