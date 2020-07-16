from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_entries'
    paginate_by = 2

