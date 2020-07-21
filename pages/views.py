from django.shortcuts import render, HttpResponse
from .counties import counties


def index(request):

    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contacts.html', {'counties': counties})
