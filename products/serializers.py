from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'is_active', 'products_count', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']
    
    def get_products_count(self, obj):
        return obj.products.filter(is_active=True).count()

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary']

class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'price', 'discount_price', 'effective_price', 'discount_percentage', 'stock_quantity', 'is_in_stock', 'image', 'category', 'category_id', 'featured', 'created_at']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    additional_images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'discount_price', 
                'effective_price', 'discount_percentage', 'stock_quantity', 
                'is_in_stock', 'image', 'additional_images', 'category', 
                'category_id', 'featured', 'sku', 'weight', 'dimensions',
                'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'sku', 'effective_price', 'discount_percentage','is_in_stock', 'created_at', 'updated_at']

class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount_price', 'stock_quantity', 'image', 'category_id', 'featured', 'weight', 'dimensions', 'is_active']
    
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value, is_active=True).exists():
            raise serializers.ValidationError("Invalid category")
        return value
    
    def validate(self, data):
        if data.get('discount_price') and data.get('price'):
            if data['discount_price'] >= data['price']:
                raise serializers.ValidationError("Discount price must be less than original price")
        return data