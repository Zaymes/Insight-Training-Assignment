from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Blog

# Create your views here.


class List(ListView):
    template_name = 'blog/home.html'
    model = Blog
    context_object_name = 'data'

class Detail(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'blog_obj'
