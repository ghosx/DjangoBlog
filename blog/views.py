from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
import markdown
import pygments
from comments.forms import CommentForm
from django.views.generic import ListView,DetailView

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5


# def detail(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     post.increase_views()  #浏览量+1
#     post.body = markdown.markdown(post.body,extensions=[
#                                      'markdown.extensions.extra',
#                                      'markdown.extensions.codehilite',
#                                      'markdown.extensions.toc',
#                                   ])
#     form = CommentForm()
#     comment_list = post.comment_set.all()
#     context = {'post': post,
#                'form': form,
#                'comment_list': comment_list
#                }
#     return render(request, 'blog/detail.html', context=context)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


# def archives(request,year,month):
#     post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )

# def category(request, category):
#     cate = get_object_or_404(Category, name=category)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, name=self.kwargs.get('category'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# def tags(request,tag):
#     a = get_object_or_404(Tag, name=tag)
#     post_list = Post.objects.filter(tags=a).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list':post_list})
class TagView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Tag,name = self.kwargs.get('tag'))
        return super(TagView,self).get_queryset().filter(tags=cate)

def about(request):
    return render(request,'about.html')

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'blog/index.html', {'error_msg': error_msg})
    post_list = Post.objects.filter(title__icontains=q)
    return render(request, 'blog/index.html', {'error_msg': error_msg,
                                               'post_list': post_list})
