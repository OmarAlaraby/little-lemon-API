from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'menuitems', views.MenuItemView, basename='menuitem')
router.register(r'catigories', views.CatigoryView, basename='catigory')

urlpatterns = [
    
] + router.urls
