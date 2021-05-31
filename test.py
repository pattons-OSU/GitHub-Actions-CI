#! python3

"""
Simeon Patton
CS362 OSU - Spring 2021
Inclass Activity week 9
GitHub actions test driver file

"""

import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.addition(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(example.subtraction(96, 3), 93)

    def test_multiplication(self):
        self.assertEqual(example.multiplication(10, 2), 20)

    def test_division(self):
        self.assertEqual(example.division(50, 2), 25)


if __name__ == '__main__':
    unittest.main()
