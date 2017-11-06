from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='类别名')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name='类别'
        verbose_name_plural=verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名')
    def __str__(self):
        return self.name
    class Meta():
        verbose_name='标签'
        verbose_name_plural=verbose_name

class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    modified_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category,verbose_name='类别')
    tags = models.ManyToManyField(Tag,blank=True,verbose_name='标签')
    author = models.ForeignKey(User,verbose_name='作者')
    views = models.PositiveIntegerField(default=0,verbose_name='浏览量')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def auto_excerpt(self):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:55]
        self.save()
    class Meta():
        verbose_name='文章'
        verbose_name_plural=verbose_name
        ordering = ['-created_time']
