from django.urls import path, include
from .views import HomeView, DashboardView, CreatePostView

urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('dashboard/', DashboardView.as_view(), name = 'user-dashboard'),
    path('create/', CreatePostView.as_view(success_url="/"), name = 'create_post'),

]
