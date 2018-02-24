from django.shortcuts import render


def index(request):
    return render(request, "flow/index.html", {})


def home(request):
    return render(request, "flow/home.html", {})


def profile(request):
    return render(request, "flow/profile.html", {})
