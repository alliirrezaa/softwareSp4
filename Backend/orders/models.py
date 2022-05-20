from django.db import models
from accounts.models import User
from home.models import Product

class OrderDetail(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    productId=models.ForeignKey(Product,on_delete=models.CASCADE)
    count=models.PositiveIntegerField()
    desc=models.TextField()
    price=models.PositiveIntegerField()
    name=models.CharField(max_length=100)
    imgfile=models.ImageField(upload_to='formDetail',null=True,blank=True)
    
    def __str__(self):
        return self.name
