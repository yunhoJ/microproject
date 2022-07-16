from django.db import models

class Shop(models.Model):
    shop_name=models.CharField(max_length=20)
    shop_address=models.CharField(max_length=40)
class Order(models.Model):
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    order_date= models.DateTimeField("date ordered")
    address= models.CharField(max_length=40)
    deliver_finished=models.BooleanField(default=0)
