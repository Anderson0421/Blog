from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.views.generic import DetailView
from .models import Like, Post

class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }   
        return render(request,'index.html',context)
    

    


class DetailPost(DetailView):
    model = Post
    template_name = 'detail.html'
    

def LikeView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_query = Like.objects.filter(user=request.user, post=post)
    if like_query.exists():
        like_query[0].delete()
        return redirect('/')
    Like.objects.create(user=request.user, post=post)
    return redirect('/')