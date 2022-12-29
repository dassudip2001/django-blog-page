from django.forms import forms
from .models import *


class Post(forms):
    class Meta:

        models=Post
        fields='__all__'