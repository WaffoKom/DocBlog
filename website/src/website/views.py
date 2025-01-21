from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForms, BlogPostForm


def index(request):
    return HttpResponse("Accueil du site")

def signup(request):
    if request.method == "POST":
        form =SignUpForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci pour l'inscription sur le site")
    else:
        form = SignUpForms()

    return  render(request, "accounts/signup.html",context={"form" :form})

def blog_post(request):
    if request.method =="POST":
        form =BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponse("Merci pour l'inscription sur le site")
    else:
        form =BlogPostForm()
    return  render(request, "blog/post.html", context={"form" :form})