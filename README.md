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
ecommerce_backend/
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

### 6. Load Sample Data (Optional)
```bash
python manage.py loaddata fixtures/sample_data.json
```

### 7. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=mysql://username:password@localhost/ecommerce_db
ALLOWED_HOSTS=localhost,127.0.0.1
```

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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


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