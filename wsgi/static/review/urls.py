from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^delete/(?P<id>[0-9]+)/$', views.deleteReview, name='deleteReview'),

]