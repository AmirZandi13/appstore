# Appstore

This is a **Django REST Framework (DRF)** project for the **Appstore**, allowing users to create and sell apps.  
Admins can verify apps before they are listed for purchase. The project is fully **Dockerized** and uses **SQLite** as the database.

## **Features**
- **User Authentication** (Signup, Login, Token-based Authentication)
- **App Management**
  - Create, View, and Purchase Apps
  - Only verified apps can be purchased
- **Admin Panel**
  - List apps with filtering options
  - Approve apps using Django Admin
- **API Documentation** using `drf-yasg`
- **Unit Tests** for app validation and admin verification

---

## **1. How to Run the Project (Using Docker)**
### **Step 1: Clone the Repository**
```sh
git clone https://github.com/AmirZandi13/appstore.git
cd appstore
```

### **Step 2: Build and Run the Docker Containers**
```sh
docker compose up --build
```
> This will start the Django app inside a Docker container and expose it at `http://127.0.0.1:8000`.

---

## **2. Database Setup & Migrations**
Since we use SQLite, no external database setup is required. Just apply migrations:
```sh
docker compose run app python manage.py migrate
```

---

## **3. Creating a Superuser (For Admin Panel)**
To access the Django admin panel (`http://127.0.0.1:8000/admin`), create a superuser:
```sh
docker compose run app python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

---

## **4. API Authentication & Getting a Token**
The API uses **JWT authentication**. To obtain a token:

```sh
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "password123"}'
```

Response:
```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```
> Use the `access` token in API requests by adding this header:  
> **`Authorization: Bearer your_access_token`**

---

## **5. Running Tests**
To run the test suite inside Docker:
```sh
docker compose run app python manage.py test
```

This will test:
- **App creation validation**
- **Admin verification logic**
- **Authentication endpoints**

---

## **6. Accessing API Documentation**
This project uses **drf-yasg** to generate API documentation.  
Once the project is running, you can access:
- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc UI:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## **7. Assumptions Made**
1. **SQLite** is used as the database to simplify deployment.
2. Only **admins can verify apps** before listing them for purchase.
3. App **verification is permanent** and does not reset after edits.
4. **Docker-only setup** (no manual Python or virtual environment setup).

---

## **8. Known Issues & Limitations**
- **SQLite is not ideal for production** (consider PostgreSQL or MySQL for scalability).
- No email verification for signups (JWT token-based authentication only).
- **File-based database:** If the `db.sqlite3` file is deleted, all data is lost.

---

## **9. Stopping & Restarting**
To stop the project:
```sh
docker compose down
```

To restart:
```sh
docker compose up --build
```

---

## **10. Debugging & Troubleshooting**
If you face issues, try running an interactive shell inside the container:
```sh
docker compose run app bash
```
Then run:
```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

---

## **11. Additional Notes**
- **Dockerfile & Docker-Compose:** Optimized for Python 3.12 and SQLite.
- **Admin actions:** Only superusers can approve apps.


