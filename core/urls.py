from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls'), name='dashboard'), 

    #Posts
    path('',HomeView.as_view(), name='Home'),
    path('<slug>/',DetailPost.as_view(), name='Detail'),


    #likes comentarios y vistas
    path('like/<slug>',LikeView, name='like'),

    path('accounts/', include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    