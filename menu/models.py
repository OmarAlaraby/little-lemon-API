from django.db import models
from django.contrib.auth.models import User

class Catigory(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    # required
    name = models.CharField(max_length=100, db_index=True)
    #url = models.CharField(max_length=255)
    
    #icon = models.ImageField(blank=True, max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, db_index=True)
    description = models.TextField(null=True)
    catigory = models.ForeignKey(Catigory , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        unique_together = ('user' , 'menu_item')
    
    def __str__(self):
        return self.user.username
        
        
class Order(models.Model):
    user = models.ForeignKey(User, related_name='Order' ,on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, verbose_name="delivery_crew", on_delete=models.SET_NULL, null=True)
    is_delivered = models.BooleanField(db_index=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.user.username
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='Items', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        unique_together = ('order' , 'item')
        
    def __str__(self):
        return self.order.id
    