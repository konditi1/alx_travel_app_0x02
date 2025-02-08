

# ALX Travel App: Milestone 3 - API Development for Listings and Bookings

This project is part of the ALX ProDev program and focuses on developing API endpoints for managing listings and bookings in a travel application. 

## Project Objectives

- Build API views to manage `Listings` and `Bookings` using Django REST Framework.
- Implement CRUD operations for both models.
- Document all API endpoints using Swagger.
- Test the endpoints for functionality.

## Project Structure

```
alx_travel_app_0x01/
├── alx_travel_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── listings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## Features

1. **Listings API**:
   - Create, Read, Update, and Delete (CRUD) operations for travel listings.

2. **Bookings API**:
   - CRUD operations for managing bookings associated with listings.

3. **Swagger Integration**:
   - Automatically generated API documentation available at `/swagger/`.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx_travel_app_0x01.git
   cd alx_travel_app_0x01
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the `alx_travel_app` directory with database credentials and other settings.

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Seed the database (optional):
   ```bash
   python manage.py seed
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the API documentation at:
   ```
   http://127.0.0.1:8000/swagger/
   ```

## Testing the API

Use a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the API endpoints:

- **Listings**: `/api/listings/`
- **Bookings**: `/api/bookings/`


