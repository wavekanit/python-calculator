import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_neg_case(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subt(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subt_neg_case(self):
        self.assertEqual(self.calc.subtract(-2, 1), -3)

    def test_multi(self) :
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_multi_neg_case(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    def test_multi_zero_case(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(3, 1), 3)

    def test_divide_neg_case(self):
        self.assertEqual(self.calc.divide(-3, 1), -3)

    def test_divide_zero_numerator_case(self):
        self.assertEqual(self.calc.divide(0, -1), 0)

    def test_divide_both_zero_case(self):
        self.assertEqual(self.calc.divide(0, 0), "undefined")

    def test_divide_zero_divider_case(self):
        self.assertEqual(self.calc.divide(3, 0), "undefined")
    
    def test_modulo(self):
        self.assertEqual(self.calc.divide(3, 2), 1)

    def test_modulo_zero_divider_case(self):
        self.assertEqual(self.calc.modulo(3, 0), "undefined")
    
    def test_modulo_zero_numerator_case(self):
        self.assertEqual(self.calc.modulo(0, 1), 0)

    def test_modulo_both_zero_case(self):
        self.assertEqual(self.calc.modulo(0, 0), "undefined")

    def test_modulo_neg_case(self):
        self.assertEqual(self.calc.modulo(5, -2), -1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()