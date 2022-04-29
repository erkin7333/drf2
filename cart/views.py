from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import DeliveryAddress, Order, OrderProduct
from .serializers import (DeliveryAddressListSerializer, DeliveryAddressSerializer,
                          OrderSerializer, OrderListSerializer)
from django.db import transaction
from django.db.models import Prefetch



class DeliveryAddressListApiview(ListAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressListSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)



class DeliveryAddressCreateApiview(CreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer


    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class DeliveryAddressEdiView(RetrieveUpdateDestroyAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)


class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.validated_data['user'] = self.request.user
            serializer.save()


class OrderListApiview(ListAPIView):
    queryset = Order.objects.prefetch_related(Prefetch("delivery_address"))
    serializer_class = OrderListSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)