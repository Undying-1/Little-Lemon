from rest_framework import serializers
from .models import Cart
from apps.MenuItems.serializers import MenuItemSerializer
from apps.Groups.serializers import UserSerializer

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem','menuitem_id', 'quantity', 'unit_price', 'price']
        
        
    def create(self, validated_data):
        return super().create(validated_data)