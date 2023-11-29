from django.urls import path
from .views import DashboardView,PostEditView,ListUsers

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard_home'),
    #CRUD Users
    path('Users/',ListUsers.as_view(), name='Users'),

    #CRUD Posts
    path('<slug>/', PostEditView.as_view(),name='Edit_post'),

]
    