from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from core.models import User,Post,Like, Comment,PostView
# Dashboard

def admin_only(function):
    def _wrapped(request, *args, **kwargs):  # Cambiado de user a request
        if request.user.has_perm('core.can_add_post_view'):
            return function(request, *args, **kwargs)
        else:
            return redirect('/')

    return _wrapped


class DashboardView(View):
    @method_decorator(login_required) #Verificamos que este iniciado sesion
    @method_decorator(admin_only) #Y que tenga los permisos para acceder

    #Colocaremos fecha y hora actual
    #La cantidad de posts
    #La cantidad de likes
    #La cantidad de comentarios y vistas

    #Ultimos 10 posts - Con Datatales


    def get(self, request, *args, **kwargs):
        hora_actual = timezone.now()
        users = User.objects.all().count()
        posts = Post.objects.all().count()
        likes = Like.objects.all().count()
        comments = Comment.objects.all().count()
        views = PostView.objects.all().count()
        post = Post.objects.all()
        context = {
            'hora':hora_actual,
            'users':users,
            'posts':posts,
            'likes':likes,
            'comments':comments,
            'views':views,
            'post':post,
        }
        return render(request, 'dashboard/index.html', context)
    