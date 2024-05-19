from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    context = {
        "articles": [
            {
                "title": "first article",
                "description": "first article description"
            },
            {
                "title": "second article",
                "description": "second article description"
            },
            {
                "title": "third article",
                "description": "third article description"
            }
        ]
    }
    return render(request, 'blog/home.html', context)


def api(request):
    data = {
        "1": {
            "id": 1,
            "title": "first article",
            "slug": "first-article",
        },
        "2": {
            "id": 2,
            "title": "second article",
            "slug": "second-article",
        },
        "3": {
            "id": 3,
            "title": "third article",
            "slug": "third-article",
        }
    }
    return JsonResponse(data)
