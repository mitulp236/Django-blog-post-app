from django.urls import path, include
from .views import HomeView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', DashboardView.as_view(), name = 'dashboard')

]
