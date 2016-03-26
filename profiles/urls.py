from django.conf.urls import url



from . import views
urlpatterns = [
	url(r'^login/$', views.loginUser, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logoutUser, name='logout'),
	url(r'^(?P<id>[0-9]+)/$', views.authorPage, name='authorPage'),
	url(r'^editProfile/(?P<id>[0-9]+)/$', views.editProfile, name='editProfile'),
] 
