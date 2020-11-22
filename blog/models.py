from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=10)
    content=models.TextField()
    author=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return "post from "+self.author
class Blogpost(models.Model):
    comments = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE)
