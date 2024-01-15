from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuItemsView.as_view()),
    path('/<int:pk>', views.SingleMenuItemView.as_view()),
]