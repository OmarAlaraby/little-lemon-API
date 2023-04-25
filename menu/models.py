from django.db import models
from django.contrib.auth.models import User

class Catigory(models.Model):
    name = models.CharField(max_length=50)

class MenuItem(models.Model):
    # required
    name = models.CharField(max_length=100)
    #url = models.CharField(max_length=255)
    
    #icon = models.ImageField(blank=True, max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True)
    catigory = models.ForeignKey(Catigory , on_delete=models.CASCADE)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        unique_together = ('user' , 'menu_item')
        
# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     delivery_crew = models.ForeignKey(User, verbose_name="delivery_crew", on_delete=models.CASCADE)
#     status = models.BooleanField(db_index=True)
#     total_price = models.FloatField(max_length=10, help_text='price in dollars', verbose_name='price', db_index=True)
#     date = models.DateTimeField(auto_now_add=True, db_index=True)
    