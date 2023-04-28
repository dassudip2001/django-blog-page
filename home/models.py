from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
# post


class Category(models.Model):
    categoryName = models.CharField(
        max_length=128, null=False, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.categoryName


class Post(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

        # Category table


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
