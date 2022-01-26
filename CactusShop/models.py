from django.db import models

# Create your models here.
class Product(models.Model) :
    ID_Product = models.CharField(max_length=10)
    Product_name = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)
    Detail_product = models.TextField(max_length=1000)
    Price = models.FloatField(max_length=10)
    Date = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.Product_name

class ProductType(models.Model):
    ProductTypeId = models.CharField(max_length=10)
    ProductTypeName = (
        (0,'Fill in'),
        (1,'Cactus'),
        (2,'Pot'),
        (3,'Potting Soil'),
        (4,'Decaration'),
        (5,'Fertilizer'),
        (6,'Seed'),
    )
    priority = models.IntegerField(default=0,choices=ProductTypeName)
    def __str__(self) -> str:
        return self.ProductTypeName

class CustomerAccount(models.Model):
    Username = models.CharField(max_length=225)
    Password = models.CharField(max_length=8)
    Email = models.CharField(max_length=225)
    def __str__(self) -> str:
        return self.Username

class Order(models.Model):
    OrderID = models.IntegerField(max_length=10)
    Date = models.DateField(auto_now=True)
    Status = models.CharField(max_length=225)
    def __int__(self) -> int:
        return self.OrderID

class Payment(models.Model):
    PaymentID = models.IntegerField(max_length=225)
    PaymentDate = models.DateField(auto_now=True)
    BankName = models.CharField(max_length=225)
    TotalPrice = models.FloatField(max_length=20)
    PaymentTime = models.DateTimeField(auto_now=True)
    def __int__(self) -> int:
        return self.PaymentID