from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
# post
class Post(models.Model):
    title=models.CharField(max_length=225,null=True,blank=True)
    
    body = RichTextField(blank=True, null=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title





#  login 

# class User(models.Model):
#     username = models.CharField(max_length=255)
#     name=models.CharField(max_length=255)
#     email=models.EmailField(max_length=255)
#     password = models.CharField(max_length=255)


# Contact us page 


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    