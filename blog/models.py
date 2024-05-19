from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):

    STATUS_CHOICES = (
        ('d', 'Draf'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title