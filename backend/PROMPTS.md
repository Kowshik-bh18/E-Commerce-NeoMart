# API Documentation

## Authentication Endpoints

### Get JWT Token

```
POST /auth/jwt/create/
{
    "username": "your_username",
    "password": "your_password"
}
```

### Register User

```
POST /auth/users/
{
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
}
```

## Product Endpoints

### List Products

```
GET /api/products/
```

### Get Product Detail

```
GET /api/products/{id}/
```

### Add to Cart

```
POST /api/products/{id}/add_to_cart/
{
    "quantity": 1
}
```

## Cart Endpoints

### List Cart Items

```
GET /api/cart/
```

### Checkout

```
POST /api/cart/checkout/
{
    "shipping_address": "Your shipping address"
}
```

## Order Endpoints

### List Orders

```
GET /api/orders/
```

### Get Order Detail

```
GET /api/orders/{id}/
```

## Category Endpoints

### List Categories

```
GET /api/categories/
```

### Get Category Detail

```
GET /api/categories/{id}/
```
