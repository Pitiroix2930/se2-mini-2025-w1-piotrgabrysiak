import unittest

from calculator import calc

class MyTestCase(unittest.TestCase):

    def test_string_returns_zero(self):
        self.assertEqual(calc(""), 0)

    def test_string_returns_self(self):
        self.assertEqual(calc("1"), 1)

    def test_numbers_split_sum(self):
        self.assertEqual(calc("1,3"),4)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, calc, "-1,3")

    def test_lage_numbers(self):
        self.assertEqual(calc("1,2,3,4,1001"),10)

    def test_delimiters(self):
        self.assertEqual(calc("//#\n1,2#3"),6)

    def test_hard_delimiters(self):
        self.assertEqual(calc("//[$%][##]$\n1##2$3$%4"),10)

if __name__ == '__main__':
    unittest.main()
