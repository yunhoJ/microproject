from hashlib import sha1
from pyexpat import model
from attr import field
from rest_framework import serializers
from user_order.models import Shop,Order

class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model=Shop
        field='__all__' 


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        field='__all__' 