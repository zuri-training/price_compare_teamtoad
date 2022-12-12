from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserPlus (AbstractUser):
   facebook_url=models.URLField(max_length=200,null=True,editable=True)
   twitter_url=models.URLField(max_length=200,null=True,editable=True)
   
   def __tuple__(self):
       return  AbstractUser.first_name, self.first_name, self.facebook_url