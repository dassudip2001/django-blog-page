from django import forms
from django.shortcuts import render

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        