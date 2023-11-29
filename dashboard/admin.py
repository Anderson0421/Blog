from django.contrib import admin
from core.models import Post,Categoria,User,Comment,Like

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(Like)
admin.site.register(Comment)