from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_entries'
    paginate_by = 2

    def get_ordering(self):
        ordering = self.request.GET.get('ordering','post_date')
        # validate ordering here
        return ordering

class DashboardView(TemplateView):
    http_method_names = ['get','post']
    template_name = "dashboard.html"
