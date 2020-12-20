from django.db import models
from django.contrib.auth.models import User



class ProductID(models.Model):
    Productid = models.CharField(max_length=200)
    def __str__(self):
        return self.Productid
    

class CustomerProd(models.Model):
    User = models.OneToOneField(User, null=True, on_delete= models.SET_NULL , )
    customerid = models.OneToOneField(ProductID, null=True, on_delete= models.SET_NULL  )
    
    def __str__(self):
        return str(self.customerid)

