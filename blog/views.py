from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})


"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""
