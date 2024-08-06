from django.urls import path
from .views import home, blog_detail, category

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('article/<slug:slug>', blog_detail, name='blog_detail'),
    path('category/<slug:slug>', category, name="category")
]