from django.shortcuts import render,get_object_or_404
from ..models import Post,Category,Tag
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
@register.simple_tag
def tags():
    return Tag.objects.all()
