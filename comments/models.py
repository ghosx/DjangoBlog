from django.db import models

# Create your models here.

class Comment(models.Model):
    """docstring for Comment."""
    name = models.CharField(max_length=100,verbose_name='用户名')
    email = models.EmailField(max_length=255,verbose_name='邮箱')
    url = models.URLField(blank=True,verbose_name='网站')
    text = models.TextField(verbose_name='留言内容')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='留言时间')
    post = models.ForeignKey('blog.Post',verbose_name='被留言文章')
    def __str__(self):
        return self.text[:25]
    class Meta():
    	verbose_name='评论'
    	verbose_name_plural=verbose_name