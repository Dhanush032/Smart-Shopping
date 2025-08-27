
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_backend.settings')
django.setup()

from frontend.views import home
from products.models import Category, Product

def run():
    # Create categories (no duplicates)
    electronics, _ = Category.objects.update_or_create(
        name='Electronics',
        defaults={'description': 'Electronic devices and gadgets'}
    )
    clothing, _ = Category.objects.update_or_create(
        name='Clothing',
        defaults={'description': 'Fashion and apparel'}
    )
    books, _ = Category.objects.update_or_create(
        name='Books',
        defaults={'description': 'Books and literature'}
    )

    # Create sample products (no duplicates)
    Product.objects.update_or_create(
        name='Smartphone',
        category=electronics,
        sku="PRD-00001",
        defaults={
            'description': 'Latest smartphone with advanced features',
            'price': 599.99,
            'discount_price': 549.99,
            'stock_quantity': 50,
            'featured': True
        }
    )
    
    
    
    Product.objects.update_or_create(
        name='Laptop',
        category=electronics,
        sku="PRD-00002",
        defaults={
            'description': 'High-performance laptop for work and gaming',
            'price': 1299.99,
            'stock_quantity': 25,
            'featured': True
        }
    )

    Product.objects.update_or_create(
        name='T-Shirt',
        category=clothing,
        sku="PRD-00003",
        defaults={
            'description': 'Comfortable cotton t-shirt',
            'price': 29.99,
            'stock_quantity': 100
        }
    )

    Product.objects.update_or_create(
        name='Python Programming Book',
        category=books,
        sku="PRD-00004",
        defaults={
            'description': 'Learn Python programming from basics to advanced',
            'price': 39.99,
            'discount_price': 29.99,
            'stock_quantity': 75,
            'featured': True
        }
    )

    Product.objects.update_or_create(
        name='Headphones',
        category=electronics,
        sku="PRD-00005",
        defaults={
            'description': 'Wireless noise-cancelling headphones',
            'price': 199.99,
            'stock_quantity': 30
        }
    )
    
    Product.objects.update_or_create(
        name ='Microwave Oven',
        category = electronics, 
        sku="PRD-00006",               
        defaults={
            'description': 'High-efficiency microwave oven with multiple power settings, defrost and grill functions, and a sleek stainless steel design.',
            'price': 7999.99,
            'discount_price': 7499.99,
            'stock_quantity': 20,
            'featured': True
        }
    )
    
    Product.objects.update_or_create(
        name='Jeans',
        category=clothing,
        sku="PRD-00007",
        defaults={
            'description': 'Comfortable and stylish denim jeans suitable for everyday wear.',
            'price': 49.99,
            'stock_quantity': 60,
            'featured': True
        }
    )

    Product.objects.update_or_create(
        name='Blender',
        category=electronics,
        sku="PRD-00008",
        defaults={
            'description': 'High-performance blender perfect for smoothies and sauces.',
            'price': 89.99,
            'stock_quantity': 40,
            'featured': True
        }
    )

    Product.objects.update_or_create(
        name='Monitor',
        category=electronics,
        sku="PRD-00009",
        defaults={
            'description': '24-inch full HD monitor with vibrant colors and sharp display.',
            'price': 299.99,
            'stock_quantity': 15,
            'featured': True
        }
    )

    Product.objects.update_or_create(
        name='Coffee Maker',
        category=electronics,
        sku="PRD-00010",
        defaults={
            'description': 'Automatic coffee maker with programmable timer and easy-to-clean design.',
            'price': 129.99,
            'stock_quantity': 25,
            'featured': True
    }
)

    Product.objects.update_or_create(
        name='Notebook',
        category=books,
        sku="PRD-00011",
        defaults={
            'description': '200-page ruled notebook suitable for school and office use.',
            'price': 9.99,
            'stock_quantity': 200,
            'featured': True
    }
)

    Product.objects.update_or_create(
        name='Jacket',
        category=clothing,
        sku="PRD-00012",
    defaults={
        'description': 'Warm and stylish jacket made with premium materials.',
        'price': 79.99,
        'stock_quantity': 35,
        'featured': True
    }
)




    print("✅ Sample data inserted without duplicates!")

if __name__ == '__main__':
    run()
