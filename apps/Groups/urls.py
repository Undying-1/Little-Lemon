from django.urls import path
from . import views

urlpatterns = [
    path('manager/users', views.UserView.as_view()),
    path('manager/users/<int:userId>', views.SingleUserView.as_view()),
    path('delivery-crew/users', views.DeliveryCrewView.as_view()),
    path('delivery-crew/users/<int:userId>', views.SingleDeliveryCrewView.as_view()),
]