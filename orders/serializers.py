from rest_framework import serializers
from django.db import transaction
from products.models import Product
from products.serializers import ProductListSerializer
from .models import Cart, CartItem, Order, OrderItem

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    subtotal = serializers.ReadOnlyField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'subtotal', 'created_at', 'updated_at']
    
    def validate_product_id(self, value):
        try:
            product = Product.objects.get(id=value, is_active=True)
            if not product.is_in_stock:
                raise serializers.ValidationError("Product is out of stock")
            return value
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found")
    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.ReadOnlyField()
    total_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_items', 'total_price', 'created_at', 'updated_at']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    subtotal = serializers.ReadOnlyField()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'user', 'status', 'total_amount', 
                'shipping_address', 'shipping_city', 'shipping_state', 
                'shipping_zip_code', 'shipping_phone', 'order_notes',
                'items', 'created_at', 'updated_at', 'shipped_at', 'delivered_at']
        read_only_fields = ['order_number', 'user', 'total_amount', 'created_at', 'updated_at', 'shipped_at', 'delivered_at']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['shipping_address', 'shipping_city', 'shipping_state', 'shipping_zip_code', 'shipping_phone', 'order_notes']
    
    def create(self, validated_data):
        user = self.context['request'].user
        
        with transaction.atomic():
            # Get user's cart
            try:
                cart = Cart.objects.get(user=user)
            except Cart.DoesNotExist:
                raise serializers.ValidationError("Cart is empty")
            
            cart_items = cart.items.all()
            if not cart_items:
                raise serializers.ValidationError("Cart is empty")
            
            # Create order
            order = Order.objects.create(
                user=user,
                total_amount=cart.total_price,
                **validated_data
            )
            
            # Create order items and update stock
            for cart_item in cart_items:
                # Check stock availability
                if cart_item.product.stock_quantity < cart_item.quantity:
                    raise serializers.ValidationError(
                        f"Insufficient stock for {cart_item.product.name}"
                    )
                
                # Create order item
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.effective_price
                )
                
                # Update product stock
                cart_item.product.stock_quantity -= cart_item.quantity
                cart_item.product.save()
            
            # Clear cart
            cart_items.delete()
            
            return order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status', 'order_notes']
    
    def validate_status(self, value):
        valid_transitions = {
            'pending': ['confirmed', 'cancelled'],
            'confirmed': ['shipped', 'cancelled'],
            'shipped': ['delivered'],
            'delivered': [],
            'cancelled': []
        }
        
        current_status = self.instance.status
        if value not in valid_transitions[current_status]:
            raise serializers.ValidationError(
                f"Cannot change status from {current_status} to {value}"
            )
        
        return value
    
    def update(self, instance, validated_data):
        status = validated_data.get('status')
        
        if status == 'shipped' and not instance.shipped_at:
            from django.utils import timezone
            instance.shipped_at = timezone.now()
        elif status == 'delivered' and not instance.delivered_at:
            from django.utils import timezone
            instance.delivered_at = timezone.now()
        
        return super().update(instance, validated_data)