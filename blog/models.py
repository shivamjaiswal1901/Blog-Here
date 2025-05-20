from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    profile_picture = models.FileField(max_length=400,null=True,upload_to='profile_images/')
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=30,null=True)
    bio = models.TextField(max_length=150,null=True)
    Dob = models.DateField(null=True)
    email = models.EmailField(max_length=50,null=True)
    mobile = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_file = models.FileField(max_length=400,upload_to='post_images/')
    post_description = models.TextField(max_length=600)
    post_created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post_title