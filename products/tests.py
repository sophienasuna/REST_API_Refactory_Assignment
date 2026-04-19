from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=10.99,
            stock=100
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(str(product), "Test Product")
