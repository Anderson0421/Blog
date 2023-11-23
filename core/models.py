from django.db import models


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
    
    def __str__(self):
        return self.title
        