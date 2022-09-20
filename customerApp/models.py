from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname


class Order(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.CharField(max_length=15)
    Customer = models.ForeignKey(Customer,related_name='order', on_delete=models.CASCADE)
