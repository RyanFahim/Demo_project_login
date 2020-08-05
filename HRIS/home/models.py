from django.db import models

# Create your models here.

# class Customer(models.Model):
#     name = models.CharField(max_length= 120, null=True)
#     phone = models.CharField(max_length= 120, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name

class Customer(models.Model):
    name = models.CharField(max_length= 120, null=True)
    phone = models.CharField(max_length= 120, null=True)
    email = models.CharField(max_length= 120, null=True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length= 120, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )

    name = models.CharField(max_length= 120, null=True)
    price = models.FloatField(null =True)
    # catergory = models.CharField(max_length= 120, null=True)
    descriptions = models.CharField(max_length= 120, null=True)
    date_created =models.DateTimeField(auto_now_add= True, null = True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
class Order(models.Model):

    STATUS =(
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered')
    )

    #making relations
    customer = models.ForeignKey(Customer, null=True ,on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    

    
