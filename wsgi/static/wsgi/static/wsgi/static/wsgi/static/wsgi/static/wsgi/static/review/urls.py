from django.urls import include, path


from . import views

urlpatterns = [
    path('delete/<int:id>/', views.deleteReview, name='deleteReview'),

]
