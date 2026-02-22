import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Creates a fresh calculator instance before every single test
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)  # 2^3
        self.assertEqual(self.calc.power(5, 0), 1)  # x^0 is 1

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(25), 5)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_history_tracking(self):
        # Perform two operations
        self.calc.add(2, 2)      # 4
        self.calc.multiply(3, 3) # 9
        
        # Check if list has 2 items
        self.assertEqual(len(self.calc.history), 2)
        
        # Check if the last operation string is correct
        last_op = self.calc.get_last_operation()
        self.assertEqual(last_op, "3 * 3 = 9")

if __name__ == '__main__':
    unittest.main()