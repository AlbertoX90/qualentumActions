import unittest
from operaciones import division,producto,sumar,restar
class TestDivision(unittest.TestCase):
 def test_division(self):
    self.assertEqual(division(4, 2), 2)
    self.assertEqual(division(-1, 0), "¡DIV/0!")
    self.assertEqual(division(-1, -1), 1)
 def test_producto(self):
    self.assertEqual(producto(3, 2), 6)
    self.assertEqual(producto(-1, 1), -1)
    self.assertEqual(producto(-1, -1), 1)
 def test_resta(self):
    self.assertEqual(restar(3, 2), 1)
    self.assertEqual(restar(-1, 1), -2)
    self.assertEqual(restar(-1, -1), 0)
 def test_suma(self):
    self.assertEqual(sumar(3, 2), 5)
    self.assertEqual(sumar(-1, 1), 0)
    self.assertEqual(sumar(-1, -1), -2)
if __name__ == '__main__':
 
 
 unittest.main()
