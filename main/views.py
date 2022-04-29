from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from .serializers import (CatrgoryListSerializer, CategorySerializer,
                          ProductListSerializer, ProductSerializer)
from .models import Category, Product


class CategoryView(APIView):

    def get(self, request):
        return Response({
        'categpry': CatrgoryListSerializer(Category.objects.all(), many=True).data
    })

    def post(self, request):
        data = CategorySerializer(data=request.data)
        if not data.is_valid():
            return Response({
                'status': 'fail',
                'data': data.errors
            })
        data.save()

        return Response({
            'status': 'success',
            'data':CatrgoryListSerializer(data.instance).data
        })


class CategoryEditSerializer(APIView):
    def get(self, request, pk):
        return Response({
            'categpry': CatrgoryListSerializer(Category.objects.get(id=pk), many=True)
        })
    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        data = CategorySerializer(data=request.data, instance=category)
        if not data.is_valid():
            return Response({
                'status': 'fail',
                'data': data.errors
            })
        data.save()

        return Response({
            'status': 'success',
            'data': CatrgoryListSerializer(data.instance).data
        })

    def delete(self, request, pk):
        Category.objects.filter(id=pk)
        return Response({
            'status': 'success'
        })


class ProductListView(ListAPIView):
    queryset = Product.objects.order_by('-added_at').all().prefetch_related('category')
    serializer_class = ProductListSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductEditView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer