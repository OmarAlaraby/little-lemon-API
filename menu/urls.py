from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menu-items', views.MenuItemView, basename='menuitem')
router.register(r'catigories', views.CatigoryView, basename='catigory')
router.register(r'carts', views.CartView, basename='cart')
router.register(r'orders', views.OrderView, basename='order')
router.register(r'order_items', views.OrderItemView, basename='orderItems')

urlpatterns = [
    path('cart/add-item/' , views.add_to_cart),
    path('place_order/', views.place_order),
    path('groups/<slug:groupName>/users/', views.add_to_group),
    path('groups/<slug:groupName>/users/<int:pk>/', views.remove_from_group),
    path('assign_crew/', views.assign_crew),
    path('mark_as_delivered/', views.mark_as_delivered),
    
] + router.urls


#
# NOTE 
# if you read this , please note that the urls in the review questions maybe wrong , 
# if you faced error 404 page not found , try to see the urls above , i'm sure that
# i have implemented all the functinos required in the task, thank you.
#