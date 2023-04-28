from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'user', 'category', 'body')
        labels = {
            'title': '',

            'body': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'level': '1', 'placeholder': 'Enter a title', 'title': 'Enter a title', 'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control', 'value': '', 'id': 'elder'}),
            'category': forms.Select(attrs={'class': 'form-control', 'value': ''}),

            'body': forms.Textarea(attrs={'class': 'form-control'}),



            #  title = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
            #   email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
            #   message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control'}))


        }
