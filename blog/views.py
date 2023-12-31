from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home_page.html', context)
