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

    def test_add_1(self):
        self.assertEqual(example.addition(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
