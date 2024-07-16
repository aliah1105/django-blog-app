from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی من"


@register.inclusion_tag('blog/partials/category_navbar.html')
def navbar():
    return {"categories": Category.objects.filter(status=True)}