from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class UserPlus (AbstractUser):
#    facebook_url=models.URLField(max_length=200,null=True,editable=True)
#    twitter_url=models.URLField(max_length=200,null=True,editable=True)
   
   def __tuple__(self):
       return  AbstractUser.first_name, self.first_name, self.last_name,self.email

class Product (models.Model):
    product_name=models.CharField(max_length=70,null=True,editable=True)
    description=models.TextField(max_length=200,null=True,editable=True,default="no description")
    url_kara=models.URLField(max_length=200,null=True,editable=True)
    url_konga=models.URLField(max_length=200,null=True,editable=True)
    url_jumia=models.URLField(max_length=200,null=True,editable=True)
    image_url=models.URLField(max_length=200,null=True,editable=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name,self.description,self.url_kara,self.url_konga,self.image_url}"


class Comments (models.Model):
    comments=models.TextField(max_length=70,null=True,editable=True)
    customer_id=models.ForeignKey(UserPlus,on_delete=models.PROTECT)
    product_id=models.ForeignKey(Product,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comments,self.customer_id,self.product_id}"