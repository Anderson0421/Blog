from core.models import Post
from django.forms import ModelForm, Select, TextInput,Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'categoria', 'slug')
        widgets = {
            'title': TextInput(attrs={'class': 'p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'author': TextInput(attrs={'class': 'p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'content': Textarea(attrs={'class': 'p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'categoria': Select(attrs={'class': 'p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
            'slug': TextInput(attrs={'class': 'p-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300'}),
        }