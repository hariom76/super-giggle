from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone_number=models.IntegerField()
    issue=models.CharField(max_length=300)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "message from " + self.name +'-'+self.email
    
