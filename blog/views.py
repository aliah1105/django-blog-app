from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello from home page!")


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
