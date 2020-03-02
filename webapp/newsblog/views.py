from django.shortcuts import render

from .models import Post, Comment


def index(request):
    post_pairs = Post.objects.order_by('-pub_date')[:11]
    post_pairs = [post_pairs[offset:2 + offset] for offset in range(0, len(post_pairs), 2)]
    context = {
        'post_pairs': post_pairs,
    }
    return render(request, 'newsblog/index.html', context)
