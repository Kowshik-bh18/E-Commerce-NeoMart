import os
import django
import random
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopverse.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

def create_sample_data():
    # Create superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Superuser created')

    # Create categories
    categories = [
        {'name': 'Electronics', 'description': 'Electronic devices and accessories'},
        {'name': 'Clothing', 'description': 'Fashion items and accessories'},
        {'name': 'Books', 'description': 'Books in various genres'},
        {'name': 'Home & Kitchen', 'description': 'Home and kitchen appliances'},
    ]

    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"Created category: {category.name}")

    # Sample products for each category
    electronics_products = [
        {'name': 'Smartphone', 'price': 599.99, 'stock': 50},
        {'name': 'Laptop', 'price': 999.99, 'stock': 30},
        {'name': 'Headphones', 'price': 99.99, 'stock': 100},
    ]

    clothing_products = [
        {'name': 'T-Shirt', 'price': 19.99, 'stock': 200},
        {'name': 'Jeans', 'price': 49.99, 'stock': 150},
        {'name': 'Sneakers', 'price': 79.99, 'stock': 100},
    ]

    books_products = [
        {'name': 'Python Programming', 'price': 39.99, 'stock': 75},
        {'name': 'Web Development Guide', 'price': 44.99, 'stock': 60},
        {'name': 'Data Science Basics', 'price': 49.99, 'stock': 80},
    ]

    home_products = [
        {'name': 'Coffee Maker', 'price': 79.99, 'stock': 40},
        {'name': 'Blender', 'price': 69.99, 'stock': 45},
        {'name': 'Toaster', 'price': 29.99, 'stock': 60},
    ]

    # Create products for each category
    for category in Category.objects.all():
        if category.name == 'Electronics':
            products = electronics_products
        elif category.name == 'Clothing':
            products = clothing_products
        elif category.name == 'Books':
            products = books_products
        else:
            products = home_products

        for prod_data in products:
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'category': category,
                    'description': f'Sample description for {prod_data["name"]}',
                    'price': Decimal(str(prod_data['price'])),
                    'stock': prod_data['stock']
                }
            )
            if created:
                print(f"Created product: {product.name}")

if __name__ == '__main__':
    print('Creating sample data...')
    create_sample_data()
    print('Sample data created successfully!')