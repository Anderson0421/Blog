from .models import Comment
from django.forms import ModelForm, TextInput,Textarea

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
        widgets = {
            'content':Textarea(attrs=({'class':'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-500 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"'}))
        }
