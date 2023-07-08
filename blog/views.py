from django.shortcuts import render
from django.generic import ListView
from .models import Post
# Create your views here.

class ListView(ListView):
    model=Post
    template_name=template