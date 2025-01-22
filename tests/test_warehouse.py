import unittest
from src.warehouse import Warehouse
from src.product import Product

class TestWarehouse(unittest.TestCase):
    def test_add_product(self):
        warehouse = Warehouse("Main Warehouse")
        product = Product(1, "Product A", 10)
        warehouse.add_product(product)
        self.assertIn(1, warehouse.inventory)

if __name__ == '__main__':
    unittest.main()
