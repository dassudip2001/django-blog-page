from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        labels = {
            'title': '',
            'body': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={})
        }
