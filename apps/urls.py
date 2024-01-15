from django.urls import path, include


urlpatterns = [
    path('groups/', include('apps.Groups.urls')),
    path('menu-items', include('apps.MenuItems.urls')),
    path('cart/', include('apps.Cart.urls')),
]