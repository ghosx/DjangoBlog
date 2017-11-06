from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id','post','name','email','url','text','created_time',)
	search_fields = ('id','post__title','name','email','url',)
admin.site.register(Comment,CommentAdmin)