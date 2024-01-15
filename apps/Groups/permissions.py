from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if Group.objects.get(name='Managers').user_set.filter(id=request.user.id).exists():
            return True
       
class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        if Group.objects.get(name='Delivery Crew').user_set.filter(id=request.user.id).exists(): 
            return True
       
class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if Group.objects.get(name='Customer').user_set.filter(id=request.user.id).exists():
            return True