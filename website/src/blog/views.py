from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .models import BlogPost


def blog_post(request):
    return redirect("https://google.com")


@login_required
def blog_post_(request):
    blogpost = get_object_or_404(BlogPost, pk=0)
    return HttpResponse(blogpost.content)



def blog_posts(request, slug):
    post = BlogPost.objects.get(slug=slug)
    post.content_word()
    return render(request, "blog/blog.html", context={"blog_posts": post})
