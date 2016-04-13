from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.gamePage, name='gamePage'),
    url(r'^postForm/$', views.posts, name='create'),
    url(r'^allPosts/(?P<id>[0-9]+)/$', views.myPosts, name='allPost'),
    url(r'^editPosts/(?P<id>[0-9]+)/$', views.editPost, name='editPost'),
    url(r'^searchResults/$', views.search, name='searchResults'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.deletePost, name='deletePost'),
]