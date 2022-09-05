from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from posts.views import index, aboutme, posts, photos, post
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('aboutme/', aboutme),
    path('posts/', posts),
    path('photos/', photos),
    path('post/', post),
    path('post/<id>/', post, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
