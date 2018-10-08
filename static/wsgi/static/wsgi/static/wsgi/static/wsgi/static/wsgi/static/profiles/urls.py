from django.urls import include, path
from . import views

urlpatterns = [
    path('login', views.loginUser, name="login"),
	path('register', views.register, name='register'),
	path('logout', views.logoutUser, name='logout'),
	path('<int:id>/', views.authorPage, name='authorPage'),#broken
	path('editProfile/<int:id>/', views.editProfile, name='editProfile'),
	path('about/', views.aboutView, name='about'),
] 
