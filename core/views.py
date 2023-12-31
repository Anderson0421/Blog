from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import View
from django.views.generic import DetailView
from .models import Like, Post,PostView
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(View):
    def get(self, request, *args, **kwargs):
        dashboardinit = request.user.has_perm('core.can_add_post_view')

        posts = Post.objects.all()
        context = {
            'posts': posts,  
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
        return object

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        
        if form.is_valid():
            post = self.get_object()
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('Detail', args=[post.slug]))

    def like_post(self, post):
        like, created = Like.objects.get_or_create(user=self.request.user, post=post)
        if not created:
            like.delete()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['form'] = CommentForm()

        if self.request.user.is_authenticated:
            liked_posts = [Like.objects.filter(user=self.request.user, post=post).exists()]
        else:
            liked_posts = []

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
