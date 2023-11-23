from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("""<html><title>Сайт Сергея Курбатова</title><h1>Сергей Курбатов</h1></html>""")
