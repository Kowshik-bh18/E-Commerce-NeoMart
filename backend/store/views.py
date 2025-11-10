from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Sum
from .models import Category, Product, CartItem, Order, OrderItem
from .serializers import (
    CategorySerializer, ProductSerializer, CartItemSerializer,
    OrderSerializer, OrderItemSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        search = self.request.query_params.get('search', None)
        
        if category:
            queryset = queryset.filter(category__id=category)
        if search:
            queryset = queryset.filter(name__icontains=search)
        
        return queryset

    @action(detail=False, methods=['get'])
    def recommendations(self, request):
        """Get product recommendations based on user's order history"""
        if not request.user.is_authenticated:
            return Response([])
            
        # Get user's order history
        ordered_products = OrderItem.objects.filter(
            order__user=request.user
        ).values_list('product__category', flat=True).distinct()
        
        # Get recommended products from same categories
        recommended = Product.objects.filter(
            category__in=ordered_products
        ).exclude(
            id__in=OrderItem.objects.filter(
                order__user=request.user
            ).values_list('product_id', flat=True)
        )[:5]
        
        serializer = self.get_serializer(recommended, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        product = self.get_object()
        user = request.user
        quantity = int(request.data.get('quantity', 1))

        if product.stock < quantity:
            return Response(
                {'error': 'Not enough stock available'},
                status=status.HTTP_400_BAD_REQUEST
            )

        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def checkout(self, request):
        cart_items = self.get_queryset()
        if not cart_items.exists():
            return Response(
                {'error': 'Cart is empty'},
                status=status.HTTP_400_BAD_REQUEST
            )

        total_amount = sum(
            item.product.price * item.quantity
            for item in cart_items
        )

        # Create order
        order = Order.objects.create(
            user=request.user,
            total_amount=total_amount,
            shipping_address=request.data.get('shipping_address', '')
        )

        # Create order items
        order_items = []
        for cart_item in cart_items:
            if cart_item.quantity > cart_item.product.stock:
                order.delete()
                return Response(
                    {'error': f'Not enough stock for {cart_item.product.name}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

            # Update product stock
            cart_item.product.stock -= cart_item.quantity
            cart_item.product.save()

        # Clear cart
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def download_invoice(self, request, pk=None):
        """Download order invoice as PDF"""
        order = self.get_object()
        from .utils import generate_invoice_pdf
        
        buffer = generate_invoice_pdf(order)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'
        response.write(buffer.getvalue())
        buffer.close()
        
        return response
