from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignUpForms


def index(request):
    return HttpResponse("Accueil du site")

def signup(request):
    form =SignUpForms()
    return  render(request, "accounts/signup.html",context={"form" :form})
