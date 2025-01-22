import unittest
from src.order import Order
from src.product import Product

class TestOrder(unittest.TestCase):
    def test_add_product_to_order(self):
        order = Order(order_id=1)
        product = Product(product_id=1, name="Product A", price=10)
        
        order.add_product(product, quantity=2)
        
        # Test if the product was added to the order
        self.assertEqual(order.items[1]['product'].name, "Product A")
        self.assertEqual(order.items[1]['quantity'], 2)

    def test_calculate_total(self):
        order = Order(order_id=1)
        product1 = Product(product_id=1, name="Product A", price=10)
        product2 = Product(product_id=2, name="Product B", price=20)
        
        order.add_product(product1, quantity=2)
        order.add_product(product2, quantity=1)
        
        # Test total calculation
        total = order.calculate_total()
        self.assertEqual(total, 40)

if __name__ == '__main__':
    unittest.main()
