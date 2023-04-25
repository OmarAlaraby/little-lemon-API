from django.shortcuts import render
from rest_framework import viewsets

# importing permissions
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAdminUser

# importing models and serializers
from .models import MenuItem , Catigory
from .serializers import MenuItemSerializer , CatigorySerialzers


class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = '__all__'
    ordering_fields = ['price']
    
class CatigoryView(viewsets.ModelViewSet):
    queryset = Catigory.objects.all()
    serializer_class = CatigorySerialzers
    permission_classes = [IsAdminUser]