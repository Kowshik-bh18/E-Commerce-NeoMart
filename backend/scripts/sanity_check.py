import os
import django
import json
import requests

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopverse.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Product, CartItem, Order

def test_flow():
    base_url = 'http://localhost:8000/api'
    
    # Step 1: Create a test user
    username = 'testuser'
    password = 'testpass123'
    email = 'test@example.com'
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password=password, email=email)
        print('Test user created')
    
    # Step 2: Get JWT token
    auth_response = requests.post(
        'http://localhost:8000/auth/jwt/create/',
        json={'username': username, 'password': password}
    )
    
    if auth_response.status_code != 200:
        print('Authentication failed')
        return
    
    token = auth_response.json()['access']
    headers = {'Authorization': f'JWT {token}'}
    
    # Step 3: List products
    products_response = requests.get(f'{base_url}/products/', headers=headers)
    if products_response.status_code != 200:
        print('Failed to fetch products')
        return
    
    products = products_response.json()['results']
    if not products:
        print('No products found')
        return
    
    # Step 4: Add first product to cart
    product = products[0]
    cart_response = requests.post(
        f'{base_url}/products/{product["id"]}/add_to_cart/',
        headers=headers,
        json={'quantity': 1}
    )
    
    if cart_response.status_code != 200:
        print('Failed to add product to cart')
        return
    
    print('Added product to cart')
    
    # Step 5: Checkout
    checkout_response = requests.post(
        f'{base_url}/cart/checkout/',
        headers=headers,
        json={'shipping_address': '123 Test St, Test City, 12345'}
    )
    
    if checkout_response.status_code != 201:
        print('Checkout failed')
        return
    
    print('Checkout successful')
    order = checkout_response.json()
    print(f'Order ID: {order["id"]}')
    print(f'Total amount: ${order["total_amount"]}')

if __name__ == '__main__':
    print('Testing basic flow...')
    test_flow()
    print('Test completed!')