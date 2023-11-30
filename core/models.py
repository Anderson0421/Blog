from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass

class Categoria(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoria')

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.CharField(max_length=150, verbose_name='Author', blank=False, null=False)
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    title = models.CharField(max_length=150,verbose_name='Title')
    content = models.TextField()
    picture = models.ImageField(upload_to='img/')
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name='post_likes', through='Like')  # Corregido aquí

    def __str__(self):
        return self.author
    
    def get_absolute_url(self):
        return reverse("Detail", kwargs={
            'slug': self.slug
    })

    def get_like_url(self):
        return reverse("like", kwargs={
            'slug':self.slug
        })
    
    @property
    def comments(self):
        return self.comment_set.all()   
    
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def get_likes_count(self):
        return self.like_set.all().count()
    
    @property
    def get_views_count(self):
        return self.postview_set.all().count()
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username