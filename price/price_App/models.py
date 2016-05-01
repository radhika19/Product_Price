from __future__ import unicode_literals
from datetime import date
from django.db import models

class Price(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField(null=True, blank=True)
    #date = models.DateTimeField()

    class Meta:
        db_table = 'price'
        
    def __str__(self):
        return str(self.price)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.ManyToManyField(Price, through = 'ProductPrice')
        
    class Meta:
       db_table = 'product'

    def __str__(self):
        return self.name

class ProductPrice(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, null=True)
    price = models.ForeignKey(Price, null=True)
    date = models.DateField(default=date.today)

    class Meta:
        db_table = 'product_price'
	
    def __str__(self):
        return self.product.name + str(self.date) + str(self.price.price)
