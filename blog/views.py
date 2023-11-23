from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'blog/home_page.html')
