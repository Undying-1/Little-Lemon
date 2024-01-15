from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from apps.Groups.permissions import IsCustomer
from apps.MenuItems.models import MenuItem
from .serializers import CartSerializer
from .models import Cart

class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsCustomer, ]
    def get_queryset(self):
        return Cart.objects.all().filter(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        username = request.user.username
        user = get_object_or_404(User, username=username)
        menu_item = get_object_or_404(MenuItem, id=request.POST.get('menuitem_id'))
        unit_price = menu_item.price 
        price = menu_item.price * int(request.POST.get('quantity'))
        try:
            Cart.objects.create(user=user,menuitem_id = request.POST.get('menuitem_id'), quantity=request.POST.get('quantity'), unit_price=unit_price, price=price)
        except:
            return JsonResponse(status=409, data={'message':"Error while creating cart"})
        return JsonResponse(status=201, data={'message':"Item added to User's cart"})
    
    def destroy(self, request, *args, **kwargs):
        username = request.user.username
        user = get_object_or_404(User, username=username)
        try:
            cart_items = Cart.objects.filter(user=user).all()
            cart_items.delete()
        except:
            return JsonResponse(status=409, data={'message':"Error while deleting from User's cart"})
        return JsonResponse(status=200, data={'message':"Items deleted from User's cart"})