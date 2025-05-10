import unittest
from Python2.day9 import Product , Cart

class TestProduct(unittest.TestCase):

    def test_product_has_name(self):
        product= Product("fan", 40, 1)
        self.assertTrue(hasattr(product, 'productName'), "Product should have a 'productName' attribute")

    def test_product_has_quantity(self):
        product= Product("fan", 40, 1)
        self.assertTrue(hasattr(product, 'quantity'), "Product should have a 'quantity' attribute")
