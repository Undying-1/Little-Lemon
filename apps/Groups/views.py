from rest_framework import generics
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name = 'Managers')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name='Managers')
            managers.user_set.add(user)
            return JsonResponse(status=201, data={'message':'User added to Managers group'})
    
    
class SingleUserView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name = 'Managers')
    serializer_class = UserSerializer
    
    def delete(self, request, userId, *args, **kwargs):
        if userId:
            user = get_object_or_404(User, pk=userId)
            managers = Group.objects.get(name='Managers')
            managers.user_set.remove(user)
            return JsonResponse(status=200, data={'message':'User removed from Managers group'})
        

class DeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
            delivery_crew = Group.objects.get(name='Delivery Crew')
            delivery_crew.user_set.add(user)
            return JsonResponse(status=201, data={'message':'User added to Delivery Crew group'})
        
        
class SingleDeliveryCrewView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    
    def delete(self, request, userId, *args, **kwargs):
        if userId:
            user = get_object_or_404(User, pk=userId)
            delivery_crew = Group.objects.get(name='Delivery Crew')
            delivery_crew.user_set.remove(user)
            return JsonResponse(status=200, data={'message':'User removed from Delivery Crew group'})
        