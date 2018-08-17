
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from posts import views as post_views #this is to avoid conflicts with other view imports

urlpatterns = [ 
    path('admin', admin.site.urls),                
    path('', post_views.index),
    path('profiles/', include('profiles.urls')),
    path('posts/',include('posts.urls')),
    path('review/',include('review.urls')),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)