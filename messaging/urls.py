from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('createMessage/<int:id>/', views.createMessage, name='createMessage'),
]