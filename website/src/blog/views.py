from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

# from django.template.loader import render_to_string
from .models import BlogPost
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView

from .forms import BlogPostForm


class BlogIndexView(ListView):
    model = BlogPost
    # queryset = BlogPost.objects.filter(publish=True)
    template_name = "blog/index.html"
    context_object_name = "articles"

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post.html"
    context_object_name = "post"
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/create_post.html"
    form_class = BlogPostForm
    success_url = reverse_lazy("blog-index")
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author =self.request.user
        form.instance.publish =True
        return  super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Creer"
        return context

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/create_post.html"
    form_class = BlogPostForm
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["submit_text"] ="Modifier"
        return  context
class BlogPostDeleteView(DetailView):
    model = BlogPost
    template_name = "blog/delete_post.html"
    context_object_name = "post"
    success_url =reverse_lazy("blog-index")

def blog_post_create(request):
    if request.method =="POST":
        form =BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.publish =True
            if request.user.is_authenticated:
                form.instance.author =request.user
            form.save()
            return  HttpResponseRedirect(reverse("blog-index"))
    else:
        form =BlogPostForm()

    return  render(request, "blog/create_post.html", {"form":form})

def blog_posts(request):
    posts = BlogPost.objects.all()
    print(posts)
    return render(request, "blog/index.html", context={"posts": posts})

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/blog.html", context={"post": post})


@login_required
def blog_post_(request):
    blogpost = get_object_or_404(BlogPost, pk=0)
    return HttpResponse(blogpost.content)