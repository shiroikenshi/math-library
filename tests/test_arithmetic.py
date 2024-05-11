# math-library-project/tests/test_arithmetic.py

import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
root_dir = os.path.dirname(parent_dir)
sys.path.append(root_dir)

import unittest
import math_library.arithmetic as arithmetic

class TestArithmeticFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(arithmetic.add(3, 5), 8)
        self.assertEqual(arithmetic.add(-2, 2), 0)
        self.assertEqual(arithmetic.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(arithmetic.subtract(10, 7), 3)
        self.assertEqual(arithmetic.subtract(-5, 2), -7)
        self.assertEqual(arithmetic.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(arithmetic.multiply(3, 5), 15)
        self.assertEqual(arithmetic.multiply(-2, 2), -4)
        self.assertEqual(arithmetic.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(arithmetic.divide(10, 2), 5)
        self.assertEqual(arithmetic.divide(9, 3), 3)
        self.assertEqual(arithmetic.divide(5, 0), float('inf'))

    def test_power(self):
        self.assertEqual(arithmetic.power(2, 3), 8)
        self.assertEqual(arithmetic.power(5, 0), 1)
        self.assertEqual(arithmetic.power(4, -2), 0.0625)

    def test_square_root(self):
        self.assertAlmostEqual(arithmetic.square_root(25), 5)
        self.assertAlmostEqual(arithmetic.square_root(16), 4)
        self.assertAlmostEqual(arithmetic.square_root(2), 1.4142135623730951)

    def test_modulo(self):
        self.assertEqual(arithmetic.modulo(10, 3), 1)
        self.assertEqual(arithmetic.modulo(15, 7), 1)
        self.assertEqual(arithmetic.modulo(20, 5), 0)

    def test_integer_division(self):
        self.assertEqual(arithmetic.integer_division(10, 3), 3)
        self.assertEqual(arithmetic.integer_division(15, 7), 2)
        self.assertEqual(arithmetic.integer_division(20, 5), 4)

    def test_minimum(self):
        self.assertEqual(arithmetic.minimum(10, 3), 3)
        self.assertEqual(arithmetic.minimum(-5, 2), -5)
        self.assertEqual(arithmetic.minimum(0, 0), 0)

    def test_maximum(self):
        self.assertEqual(arithmetic.maximum(10, 3), 10)
        self.assertEqual(arithmetic.maximum(-5, 2), 2)
        self.assertEqual(arithmetic.maximum(0, 0), 0)

    def test_round_number(self):
        self.assertEqual(arithmetic.round_number(3.14159, 2), 3.14)
        self.assertEqual(arithmetic.round_number(6.5), 6)
        self.assertEqual(arithmetic.round_number(9.87654, 3), 9.877)

if __name__ == '__main__':
    unittest.main()