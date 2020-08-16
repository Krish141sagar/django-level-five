from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    Name=models.CharField(max_length=256)
    Email=models.EmailField(max_length=256)
    Mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.Name;

class  PortfoiloModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfoilo=models.URLField(max_length=200,blank=True)
    Image_link=models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username
