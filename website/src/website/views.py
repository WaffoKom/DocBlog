from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForms, BlogPostForm
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name ="index.html"
    title ="Default"
    def get_context_data(self, **kwargs):
         context =super().get_context_data(**kwargs)
         context["title"]=self.title
         return context


def home(request):
    return render(request, "index.html", {"title" :"Accueil du site"})

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