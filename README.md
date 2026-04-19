🛍 Inventory & Order Management API — Django REST + Swagger

## 📌 Overview

This project is a RESTful API built with Django and Django REST Framework (DRF) for managing:

- Products
- Vendors
- Clients
- Orders

The system demonstrates relational data modeling and scalable API design, with interactive documentation powered by Swagger (OpenAPI).

## 🚀 Features

- 📦 Product management (CRUD)
- 🏢 Vendor management
- 👥 Client management
- 🧾 Order management (linked to products, clients, and vendors)
- 🔄 RESTful API architecture
- 🧪 Interactive API testing with Swagger
- 📄 Auto-generated API documentation

🏗 Tech Stack
Backend: Django 6
API Framework: Django REST Framework (DRF)
Documentation: drf-yasg (Swagger / OpenAPI)
Database: SQLite (default)
Language: Python 3.12+

📂 Project Structure
core/
│── settings.py
│── urls.py
│
products/
│── models.py
│── serializers.py
│── views.py
│── urls.py

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/products-api.git
cd products-api
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run migrations
python manage.py migrate
5️⃣ Start the server
python manage.py runserver

6️⃣ Run tests
python manage.py test

## 🌐 API Endpoints

### 📦 Products

- GET `/api/v1/products/`
- POST `/api/v1/products/`
- GET `/api/v1/products/{id}/`
- PUT/PATCH `/api/v1/products/{id}/`
- DELETE `/api/v1/products/{id}/`

### 🏢 Vendors

- GET `/api/v1/vendors/`
- POST `/api/v1/vendors/`
- GET `/api/v1/vendors/{id}/`
- PUT/PATCH `/api/v1/vendors/{id}/`
- DELETE `/api/v1/vendors/{id}/`

### 👥 Clients

- GET `/api/v1/clients/`
- POST `/api/v1/clients/`
- GET `/api/v1/clients/{id}/`
- PUT/PATCH `/api/v1/clients/{id}/`
- DELETE `/api/v1/clients/{id}/`

### 🧾 Orders

- GET `/api/v1/orders/`
- POST `/api/v1/orders/`
- GET `/api/v1/orders/{id}/`
- PUT/PATCH `/api/v1/orders/{id}/`
- DELETE `/api/v1/orders/{id}/`

## 🔗 Data Relationships

- An **Order** is linked to:
  - a Product
  - a Client
  - a Vendor

This demonstrates relational database design using foreign keys.

🧪 Swagger API Documentation
Interactive API documentation is available at:
http://127.0.0.1:8000/swagger/

Alternative documentation view:
http://127.0.0.1:8000/redoc/

🔍 Using Swagger
Open /swagger/
Select an endpoint (e.g. POST /api/v1/products/)
Click "Try it out"
Enter request data:
{
"name": "Laptop",
"description": "Gaming laptop",
"price": "1200.00",
"stock": 10
}

Click Execute
📄 Example Response
{
"id": 1,
"name": "Laptop",
"description": "Gaming laptop",
"price": "1200.00",
"stock": 10
}

🔐 Authentication
Currently, the API allows unrestricted access for development:

permission_classes = [AllowAny]

Future improvements may include:
JWT Authentication
Role-based access control
📈 Future Enhancements
🔐 Authentication & Authorization (JWT)
🔍 Filtering & Search
📄 Pagination
🏷 Category management
📊 Analytics endpoints

💡 Why Swagger?
This project uses Swagger because it provides:

- Automatic API documentation
- Clear request/response structure
- Better frontend-backend collaboration
- 🤝 Contribution
- Interactive API testing
