# Cinema Paradiso Backend 🎥🎬

This is the backend API for the **Cinema Paradiso** project, built with Django. It provides endpoints for managing movies, user authentication, and other related services.

---

## **Features**
- RESTful API built with Django and Django REST Framework (DRF).
- Movie management: add, update, delete, and retrieve movie information.
- Integration with Cloudinary for media file uploads.
- Configurable settings for development and production environments.

---

## **Getting Started**

### **Prerequisites**
- Python 3.10 or higher.
- Django installed (`pip install django`).
- PostgreSQL (or your preferred database).
- Cloudinary account for media storage.

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cinema-paradiso-backend.git
   cd cinema-paradiso-backend
   
   python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your_database_connection_string
CLOUD_NAME=your_cloudinary_cloud_name
CLOUD_API_KEY=your_cloudinary_api_key
CLOUD_API_SECRET=your_cloudinary_api_secret
python manage.py migrate
python manage.py runserver

 Or run on replit: https://replit.com/@huemig/Cinema-Paradiso-backend 
 

