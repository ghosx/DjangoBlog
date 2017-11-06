from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
    url(r'^category/(?P<category>[0-9a-zA-Z\s]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<tag>[0-9a-zA-Z\s]+)/$',views.TagView.as_view(),name='tag'),
    url(r'^about/$',views.about,name='about'),
    url(r'^search/$', views.search, name='search'),
]
