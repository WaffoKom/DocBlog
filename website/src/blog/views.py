from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import BlogPost


def blog_post(request):
    return redirect("https://google.com")


def blog_posts(request,slug):
    post = BlogPost.objects.get(slug =slug)
    return render(request, "blog/blog.html", context={"blog_posts":post})





