from django.forms import forms
from blog.models import Comment

class CommentForm(forms.Form):

    class Meta:
        model = Comment
        exclude = ['post', 'created_at']