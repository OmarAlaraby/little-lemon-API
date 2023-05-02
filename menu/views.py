from django.shortcuts import render
from rest_framework import viewsets

# decorators
from rest_framework.decorators import api_view , permission_classes

# Helpers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# importing permissions
from .permissions import IsAdminOrReadOnly , IsAdminOrAuthenticated , IsAdminOrDeliveryCrew
from rest_framework.permissions import IsAdminUser

# importing models and serializers
from .models import MenuItem , Catigory , Cart , Order , OrderItem
from .serializers import MenuItemSerializer , CatigorySerialzers , CartSerializer , OrderSerializer, OrderItemSerializer
from django.contrib.auth.models import User , Group


class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = '__all__'
    ordering_fields = ['price', 'catigory']
    
class CatigoryView(viewsets.ModelViewSet):
    queryset = Catigory.objects.all()
    serializer_class = CatigorySerialzers
    permission_classes = [IsAdminOrReadOnly]
    
class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAdminOrAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cart.objects.all()
        return Cart.objects.filter(user=user)
    
class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrAuthenticated]
    
    # need to set a filter in the view
    
    def get_queryset(self):
        user = self.request.user
        
        if user.groups.filter(name='Managers').exists():
            return Order.objects.all()
        elif user.groups.filter(name='Delivery Crew').exists():
            return Order.objects.filter(delivery_crew=user)
        
        return Order.objects.filter(user=user)
    
class OrderItemView(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminOrAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return OrderItem.objects.all()
        return OrderItem.objects.filter(order__user=user)
    
    
# assign user to a group
@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def add_to_group(request, slug):
    user_id = request.data['userId']
    
    
    user = get_object_or_404(User, id=user_id)
    group = get_object_or_404(Group, name=slug)
    
    if request.method == 'POST':
        user.groups.add(group)
        return Response({"message" : "user added"}, status.HTTP_201_CREATED)
    else:
        user.groups.remove(group)
        return Response({"message" : "user removed"}, status.HTTP_201_CREATED)
    
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def remove_from_group(requset , slug , pk):
    user = get_object_or_404(User, id=pk)
    group = get_object_or_404(Group , name=slug)
    
    user.groups.remove(group)
    return Response({"Response" : "User Removed"} , status.HTTP_200_OK)
    

# add to cart function
@api_view(['POST'])
@permission_classes([IsAdminOrAuthenticated])
def add_to_cart(request):
    item_id = request.data['itemId']
    quantity = request.data['quantity']
    
    user = request.user
    item = get_object_or_404(MenuItem , id=item_id)
    Cart.objects.create(    user= user,
                            menu_item= item,
                            quantity= quantity ,
                            unit_price= item.price ,
                            total_price= int(item.price) * int(quantity)
                        )
    return Response({"Response" : "item added successfully"} ,status.HTTP_201_CREATED)


# place the order
@api_view(['POST'])
@permission_classes([IsAdminOrAuthenticated])
def place_order(request):
    user = request.user
    cart_items = user.cart.all()
    
    if len(cart_items) == 0:
        return Response({"Response" : "no items to order"} , status.HTTP_400_BAD_REQUEST)
    
    order = Order(user = user , is_delivered = False, total_price=0)
    order.save()
    
    total_price = 0
    for item in cart_items:
        total_price += item.total_price
        OrderItem(
            order = order,
            item = item.menu_item,
            quantity = item.quantity,
            unit_price = item.unit_price,
            total_price = item.total_price
        ).save()
    
    cart_items.delete()
    order.total_price = total_price
    order.save()
    
    return Response({"Response" : "Order Placed"}, status.HTTP_201_CREATED)


# for manager , assign crew to orders
@api_view(['POST'])
@permission_classes([IsAdminUser])
def assign_crew(request):
    user_id = request.data['userId']
    order_id = request.data['orderId']
    
    user = get_object_or_404(User , id=user_id)
    order = get_object_or_404(Order , id=order_id)
    
    if not user.groups.filter(name='Delivery Crew').exists():
        return Response({"Response" : "user is not a Delivery Crew"}, status.HTTP_400_BAD_REQUEST)
    
    order.delivery_crew = user
    order.save()
    
    return Response({"Response" : "Crew Assigned"}, status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminOrDeliveryCrew])
def mark_as_delivered(request):
    order_id = request.data['orderId']
    
    order = get_object_or_404(Order , id=order_id)
    
    if order.is_delivered:
        return Response({"Response" : "Order Is Already Been Deliverd"} , status.HTTP_400_BAD_REQUEST)
    
    order.is_delivered = True
    order.save()
    
    return Response({"Response" : "Order Marked As Delivered"}, status.HTTP_200_OK)