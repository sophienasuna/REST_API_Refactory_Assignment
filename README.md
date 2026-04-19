🛍 Products API — Django REST + Swagger
📌 Overview

The Products API is a RESTful backend service built with Django and Django REST Framework (DRF) for managing product data.

It provides endpoints to create, retrieve, update, and delete products, along with auto-generated API documentation using Swagger (OpenAPI).

This project demonstrates modern backend development practices including:

- RESTful API design
- Serializer-based data validation
- Class-based generic views
- Interactive API documentation

🚀 Features

- 📦 Product CRUD Operations
- 🔄 RESTful API endpoints
- 🧪 Built-in API testing via Swagger UI
- 📄 Auto-generated API documentation (OpenAPI)
- 🧱 Clean and scalable DRF architecture

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

🌐 API Endpoints
🔹 Base URL
http://127.0.0.1:8000/

📦 Products
Method Endpoint Description
GET /api/v1/products/ List all products
POST /api/v1/products/ Create a product
GET /api/v1/products/{id}/ Retrieve product
PUT /api/v1/products/{id}/ Update product
PATCH /api/v1/products/{id}/ Partial update
DELETE /api/v1/products/{id}/ Delete product

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
