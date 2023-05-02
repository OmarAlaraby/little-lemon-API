from rest_framework import serializers
from .models import MenuItem, Catigory , Cart, Order , OrderItem


class CatigorySerialzers(serializers.ModelSerializer):
    
    class Meta:
        model = Catigory
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    
    try:
        unclassified = Catigory.objects.get(name='unclassified')
    except:
        unclassified = Catigory.objects.create(name='unclassified')
    
    catigory = serializers.PrimaryKeyRelatedField(
        queryset = Catigory.objects.all(),
        default = unclassified
    )
    
    class Meta:
        model = MenuItem
        fields = '__all__'
        
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'