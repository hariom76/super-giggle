from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=10)
    content=models.TextField()
    author=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return "post from "+self.author
    
    