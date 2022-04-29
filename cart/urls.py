from django.urls import path

from .views import (DeliveryAddressListApiview, DeliveryAddressCreateApiview,
                    DeliveryAddressEdiView)
from .views import (OrderCreate, OrderListApiview)

app_name = 'cart'

urlpatterns = [
    path('delivery-address/', DeliveryAddressListApiview.as_view(), name='delivery-address'),
    path('create-address/', DeliveryAddressCreateApiview.as_view(), name='create-address'),
    path('delivery-address/<int:pk>/', DeliveryAddressEdiView.as_view(), name='delivery-address-edit'),

    path('orders/', OrderListApiview.as_view(), name='orders'),
    path('order/', OrderCreate.as_view(), name="order")
]