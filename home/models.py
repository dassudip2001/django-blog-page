from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
# post
class Post(models.Model):
    title=models.CharField(max_length=225,null=True,blank=True)
    photo= models.ImageField(upload_to="my_post")
    Body = RichTextField(blank=True, null=True)
    date=models.DateField(auto_now_add=True)



#  login 

# class User(models.Model):
#     username = models.CharField(max_length=255)
#     name=models.CharField(max_length=255)
#     email=models.EmailField(max_length=255)
#     password = models.CharField(max_length=255)
    