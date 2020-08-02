from django.urls import path, include
from .views import BlogView, AddBlogPostView, UsersBlogView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name = 'user-dashboard'),
    path('myblogs/', UsersBlogView.as_view(), name = 'my-blogs'),
    path('create/', AddBlogPostView.as_view(), name = 'create-blog-post'),
]
