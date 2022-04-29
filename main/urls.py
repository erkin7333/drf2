from django.urls import path
from .views import (CategoryView, CategoryEditSerializer,
                    ProductListView, ProductCreateView,
                    ProductEditView)



app_name = "main"

urlpatterns = [
    path('category/', CategoryView.as_view(), name='categpry'),
    path('category/<int:pk>/', CategoryEditSerializer.as_view(), name='category-edit'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/', ProductCreateView.as_view(), name='product'),
    path('product/<int:pk>/', ProductEditView.as_view(), name='product-edit'),
]