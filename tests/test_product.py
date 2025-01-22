import sys
import os




# Add the src directory to the system path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from product import Product


import unittest


class TestProduct(unittest.TestCase):
    def test_update_quantity(self):
        product = Product(1, "Product A", 10)
        product.update_quantity(5)
        self.assertEqual(product.quantity, 15)
        product.update_quantity(-3)
        self.assertEqual(product.quantity, 12)

if __name__ == '__main__':
    unittest.main()
