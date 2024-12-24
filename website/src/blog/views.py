from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import BlogPost


def blog_posts(request):
    posts = BlogPost.objects.all()
    print(posts)
    return render(request, "blog/index.html", context={"blog_posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/blog.html", context={"post": post})


@login_required
def blog_post_(request):
    blogpost = get_object_or_404(BlogPost, pk=0)
    return HttpResponse(blogpost.content)
