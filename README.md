# E-Commerce Backend System with Django REST Framework

A comprehensive e-commerce backend system built with Django and Django REST Framework, featuring JWT authentication, product management, order processing, and a Bootstrap-based frontend.

## 🚀 Features

### Backend Features
- **JWT Authentication** using SimpleJWT with role-based access (Admin/Customer)
- **Product Management System** with categories, pricing, and inventory tracking
- **Shopping Cart & Order Management** with complete order lifecycle
- **MySQL Database Support** with optimized models and relationships
- **RESTful API** with comprehensive serializers, views, and permissions
- **Swagger Documentation** using drf-spectacular
- **Admin Dashboard** with Django Admin integration
- **Role-based Permissions** for secure API access

### Frontend Features
- **Bootstrap 5 Responsive Design** with modern UI/UX
- **Product Catalog** with search, filtering, and pagination
- **Shopping Cart System** with quantity management
- **User Authentication** with login/register forms
- **Order Management** with status tracking
- **Admin Dashboard** for managing products and orders
- **Mobile-Responsive Design** optimized for all devices

## 🛠 Technology Stack

**Backend:**
- Django 4.2.7
- Django REST Framework 3.14.0
- SimpleJWT for JWT authentication
- MySQL database with mysqlclient
- drf-spectacular for API documentation
- Pillow for image handling

**Frontend:**
- Bootstrap 5.3.0
- Vanilla JavaScript with Fetch API
- Font Awesome icons
- Responsive CSS Grid/Flexbox

## 📁 Project Structure

```
Smart Shopping/
├── accounts/              # User authentication & profiles
├── products/             # Product & category management
├── orders/              # Cart & order processing
├── frontend/            # URL routing for templates
├── templates/           # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
├── ecommerce_backend/  # Main project settings
└── manage.py           # Django management script
```

## 🚦 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ecommerce-backend
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup

**Option A: MySQL (Recommended for Production)**
```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE ecommerce_db;
CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
FLUSH PRIVILEGES;
```

**Option B: SQLite (For Development)**
Uncomment SQLite configuration in `settings.py` and comment MySQL configuration.

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```


### 6. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📚 API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/`
- **ReDoc**: `http://127.0.0.1:8000/api/redoc/`
- **Django Admin**: `http://127.0.0.1:8000/admin/`

## 🔐 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `GET /api/auth/profile/` - Get user profile
- `PUT /api/auth/profile/` - Update user profile
- `POST /api/auth/change-password/` - Change password

### Products
- `GET /api/products/` - List products (with filtering)
- `POST /api/products/` - Create product (Admin only)
- `GET /api/products/{slug}/` - Get product details
- `PUT /api/products/{slug}/` - Update product (Admin only)
- `DELETE /api/products/{slug}/` - Delete product (Admin only)
- `GET /api/products/featured/` - Get featured products
- `GET /api/products/low_stock/` - Get low stock products (Admin only)

### Categories
- `GET /api/products/categories/` - List categories
- `POST /api/products/categories/` - Create category (Admin only)
- `GET /api/products/categories/{slug}/` - Get category details
- `PUT /api/products/categories/{slug}/` - Update category (Admin only)
- `DELETE /api/products/categories/{slug}/` - Delete category (Admin only)

### Cart & Orders
- `GET /api/orders/cart/1/` - Get user's cart
- `POST /api/orders/cart/add_item/` - Add item to cart
- `PUT /api/orders/cart/update_item/` - Update cart item
- `DELETE /api/orders/cart/remove_item/` - Remove cart item
- `DELETE /api/orders/cart/clear/` - Clear cart
- `GET /api/orders/orders/` - List orders
- `POST /api/orders/orders/create_order/` - Create order from cart
- `GET /api/orders/orders/{id}/` - Get order details
- `PUT /api/orders/orders/{id}/update_status/` - Update order status (Admin only)

## 🎨 Frontend Pages

- **Home** (`/`) - Landing page with featured products
- **Products** (`/products/`) - Product catalog with search & filters
- **Cart** (`/cart/`) - Shopping cart management
- **Login** (`/login/`) - User authentication
- **Register** (`/register/`) - User registration
- **Profile** (`/profile/`) - User profile management
- **Orders** (`/orders/`) - Order history and tracking
- **Admin Dashboard** (`/admin-dashboard/`) - Admin management interface

## 🔧 Configuration


### Settings Configuration
Key settings in `ecommerce_backend/settings.py`:
- JWT token configuration
- CORS settings for frontend
- Database configuration
- Static files handling
- Media files configuration

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts
python manage.py test products
python manage.py test orders

# Coverage report
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 📦 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure production database
3. Set up static files serving
4. Configure ALLOWED_HOSTS
5. Set up SSL/HTTPS
6. Configure email backend
7. Set up logging
8. Use environment variables for sensitive data
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙋‍♂️ Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the API documentation for usage details

## 🔮 Future Enhancements

- Payment gateway integration (Stripe/PayPal)
- Email notifications for orders
- Product reviews and ratings
- Wishlist functionality
- Advanced inventory management
- Multi-vendor support
- Real-time notifications
- Mobile app API endpoints
- Analytics and reporting dashboard
- Social authentication
- Product recommendations
- Coupon and discount system

---

**Built with ❤️ using Django REST Framework**

This project demonstrates modern backend development practices with Django, including proper API design, authentication, database modeling, and frontend integration. Perfect for learning full-stack web development or as a foundation for commercial e-commerce applications.
