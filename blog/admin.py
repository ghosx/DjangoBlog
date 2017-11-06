from django.contrib import admin
from .models import Post,Category,Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_time', 'modified_time', 'category','author',)
    search_fields = ('id','title','category__name','tags__name','author__username',)
    list_editable = ('title','category',)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','name',)
	list_editable = ('name',)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id','name',)
	list_editable = ('name',)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
