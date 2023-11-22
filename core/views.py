from django.shortcuts import render
from django.views.generic import View
from .models import Post

class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }   
        return render(request,'index.html',context)