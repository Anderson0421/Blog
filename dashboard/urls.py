from django.urls import path
from .views import DashboardView,NewPost

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard_home'),
    path('new/', NewPost.as_view(), name='new_post'),

]
