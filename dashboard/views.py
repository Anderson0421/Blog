from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import View,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from core.models import User,Post,Like, Comment,PostView


# Dashboard

#Traemos el formulario
from .forms import PostForm

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
        form = PostForm()
        hora_actual = timezone.now()
        lastlogin = request.user.last_login
        users = User.objects.all().count()
        posts = Post.objects.all().count()
        likes = Like.objects.all().count()
        comments = Comment.objects.all().count()
        views = PostView.objects.all().count()
        post = Post.objects.all()
        context = {
            'hora':hora_actual,
            'last_login':lastlogin,
            'users':users,
            'posts':posts,
            'likes':likes,
            'comments':comments,
            'views':views,
            'post':post,
            'form':form,
        }
        return render(request, 'dashboard/index.html', context)
    
    def post(self,request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
        else:
            return redirect('/dashboard/')


class PostEditView(View):
    @method_decorator(login_required)
    @method_decorator(admin_only)
    
    def get(self, request,slug, *args, **kwargs):
        post = get_object_or_404(Post,slug=slug)
        form = PostForm(instance=post)
        context = {
            'form':form
        }
        return render(request,'dashboard/detail.html',context)
    

    def post(self, request,slug, *args, **kwargs):
        post = get_object_or_404(Post,slug=slug)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
        else:
            return redirect('/dashboard/')


class DeleteView(DeleteView):
    model = Post
    template_name = 'dashboard/delete.html'
    success_url =  reverse_lazy('dashboard_home')


class ListUsers(View):
    def get(self,request,*args,**kwargs):
        Usuarios = User.objects.all()
        context = {
            'users':Usuarios
        }
        return render(request,'dashboard/users/users.html',context)