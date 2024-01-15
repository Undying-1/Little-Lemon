from django.db import models
from django.contrib.auth.models import User

from apps.MenuItems.models import MenuItem

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return self.user.get_username()
    
    class Meta:
        unique_together = ('menuitem', 'user')
        
    
    
