from rest_framework import generics, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import Category, Product
from .serializers import (
    CategorySerializer, 
    ProductListSerializer, 
    ProductDetailSerializer,
    ProductCreateUpdateSerializer
)
from .permissions import IsAdminOrReadOnly

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']
    
    @extend_schema(
        summary="List Categories",
        description="Retrieve a list of all active categories"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Create Category",
        description="Create a new product category (Admin only)"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured', 'is_active']
    search_fields = ['name', 'description', 'sku']
    ordering_fields = ['name', 'price', 'created_at', 'stock_quantity']
    ordering = ['-created_at']
    lookup_field = 'slug'
    
    def get_queryset(self):
        queryset = Product.objects.select_related('category')
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        # Filter by availability
        in_stock = self.request.query_params.get('in_stock')
        if in_stock == 'true':
            queryset = queryset.filter(stock_quantity__gt=0)
        elif in_stock == 'false':
            queryset = queryset.filter(stock_quantity=0)
        
        # For non-admin users, only show active products
        if not (self.request.user.is_authenticated and self.request.user.is_admin):
            queryset = queryset.filter(is_active=True)
        
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ProductCreateUpdateSerializer
        return ProductDetailSerializer
    
    @extend_schema(
        summary="List Products",
        description="Retrieve a list of products with filtering and search capabilities",
        parameters=[
            OpenApiParameter('category', int, description='Filter by category ID'),
            OpenApiParameter('min_price', float, description='Minimum price filter'),
            OpenApiParameter('max_price', float, description='Maximum price filter'),
            OpenApiParameter('in_stock', bool, description='Filter by stock availability'),
            OpenApiParameter('featured', bool, description='Filter featured products'),
            OpenApiParameter('search', str, description='Search in name and description'),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Create Product",
        description="Create a new product (Admin only)"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products"""
        queryset = self.get_queryset().filter(featured=True, is_active=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        
        serializer = ProductListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Get products with low stock (Admin only)"""
        if not (request.user.is_authenticated and request.user.is_admin):
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        threshold = int(request.query_params.get('threshold', 10))
        queryset = self.get_queryset().filter(stock_quantity__lte=threshold, is_active=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        
        serializer = ProductListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)