from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.gamePage, name='gamePage'),
    path('postForm/', views.posts, name='create'),
    path('allPosts/<int:id>/', views.myPosts, name='allPost'),
    path('editPosts/<int:id>/', views.editPost, name='editPost'),
    path('searchResults/', views.search, name='searchResults'),
    path('delete/<int:id>/', views.deletePost, name='deletePost'),
]
 