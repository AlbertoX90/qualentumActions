import unittest
from operaciones import producto
class TestProducto(unittest.TestCase):
 def test_producto(self):
    self.assertEqual(producto(3, 2), 6)
    self.assertEqual(producto(-1, 1), -1)
    self.assertEqual(producto(-1, -1), 1)
if __name__ == '__main__':
 unittest.main()
