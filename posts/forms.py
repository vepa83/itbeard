"""
from django.forms import ModelForm 
from . models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        labels = {'author':'Ваше Имя', 'text':'текст отзыва' }
"""