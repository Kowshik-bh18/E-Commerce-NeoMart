from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from .models import Category, Product, CartItem, Order

class StoreAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        # Create test category
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        
        # Create test product
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            description='Test Description',
            price=Decimal('99.99'),
            stock=10
        )

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_add_to_cart(self):
        response = self.client.post(
            f'/api/products/{self.product.id}/add_to_cart/',
            {'quantity': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CartItem.objects.count(), 1)

    def test_checkout(self):
        # Add item to cart first
        cart_item = CartItem.objects.create(
            user=self.user,
            product=self.product,
            quantity=1
        )
        
        response = self.client.post(
            '/api/cart/checkout/',
            {'shipping_address': '123 Test St'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(CartItem.objects.count(), 0)  # Cart should be cleared
