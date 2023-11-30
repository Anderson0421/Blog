from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import View
from django.views.generic import DetailView
from .models import Like, Post,PostView
from .forms import CommentForm




class HomeView(View):
    def get(self, request, *args, **kwargs):
        dashboardinit = request.user.has_perm('core.can_add_post_view')

        posts = Post.objects.all()
        liked_posts = []

        for post in posts:
            if request.user.is_authenticated:
                like_query = Like.objects.filter(user=request.user, post=post)
                liked = like_query.exists()
                liked_posts.append({'liked': liked})

        context = {
            'posts': posts,  
            'likes':liked_posts,
            'dashboardinit': dashboardinit,
        }   
        return render(request, 'post/index.html', context)
    

class DetailPost(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_object(self, *kwargs):
        object = super().get_object(*kwargs)
        if self.request.user.is_authenticated: 
            PostView.objects.get_or_create(user=self.request.user, post=object)
        else:
            return redirect('/')
        return object
    
    
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        
        if form.is_valid():
            post = self.get_object()
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('Detail', args=[post.slug]))  # Asegúrate de incluir el slug en la redirección

        
    def get_context_data(self, **kwargs):
        posts = Post.objects.all()
        liked_posts = []
        for post in posts:
            like_query = Like.objects.filter(user=self.request.user, post=post)
            liked = like_query.exists()
            liked_posts.append({'liked': liked})
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['likes'] = liked_posts
        return context
    

def LikeView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_query = Like.objects.filter(user=request.user, post=post)

    if like_query.exists():
        like_query[0].delete()
        liked = False
    else:
        Like.objects.create(user=request.user, post=post)
        liked = True

    return HttpResponseRedirect(reverse('Home'))
