from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('sendMessage/<int:id>/', views.sendMessage, name='sendMessage'),
]