from django.contrib import admin
from .models import Cart , Order , MenuItem , OrderItem

admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(MenuItem)
