from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignUpForms


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
