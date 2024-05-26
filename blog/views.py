from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    context = {
        "articles": Article.objects.filter(status="p").order_by('-publish')
    }
    return render(request, 'blog/index.html', context)


def blog_detail(request, slug):
    context = {
        'article': Article.objects.get(slug=slug)
    }

    return render(request, 'blog/post.html', context)
