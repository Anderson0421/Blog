from django.urls import path
from .views import DashboardView,PostEditView,ListUsers,DeleteView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard_home'),
    #CRUD Users
    path('Users/',ListUsers.as_view(), name='Users'),

    #CRUD Posts
    path('<slug>/', PostEditView.as_view(),name='Edit_post'),

    path('Delete/<slug>/',DeleteView.as_view(),name='Delete_post'),

]
    