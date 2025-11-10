# NeoMart

A full-stack e-commerce application built with Django REST Framework and React.

## Features

- User authentication with JWT
- Product catalog with categories
- Shopping cart functionality
- Order management
- Product recommendations
- Invoice generation
- Search and filtering

## Tech Stack

### Backend

- Django
- Django REST Framework
- SimpleJWT for authentication
- drf-yasg for API documentation
- SQLite database

### Frontend

- React
- Chakra UI
- React Router
- Axios

## Setup

### Backend Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Load sample data:

```bash
python scripts/seed.py
```

6. Start the development server:

```bash
python manage.py runserver
```

### Frontend Setup

1. Install dependencies:

```bash
cd frontend
npm install
```

2. Start the development server:

```bash
npm start
```

## API Documentation

API documentation is available at:

- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Testing

To run backend tests:

```bash
cd backend
python manage.py test
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
