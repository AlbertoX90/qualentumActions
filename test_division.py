import unittest
from operaciones import division
class TestDivision(unittest.TestCase):
 def test_division(self):
    self.assertEqual(division(4, 2), 2)
    self.assertEqual(division(-1, 0), "¡DIV/0!")
    self.assertEqual(division(-1, -1), 1)
if __name__ == '__main__':
 unittest.main()
