from django.db import models
from django.utils import timezone
from extentions.utils import jalali_convertor

# Create your models here.

class Article(models.Model):

    STATUS_CHOICES = (
        ('d', 'Draf'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to="images", verbose_name='تصویر')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = 'زمان انتشار'
    
    def __str__(self) -> str:
        return self.title