from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, TemplateView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_entries'
    paginate_by = 3

    def get_ordering(self):
        ordering = self.request.GET.get('ordering','-post_date')
        # validate ordering here
        return ordering

class DashboardView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "dashboard.html"
    context_object_name = 'post_entries'
    paginate_by = 3
    
    def get_queryset(self):
        return Post.objects.filter(post_author = self.request.user)

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ['post_title','post_text' ]

    def form_valid(self,form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)
    
