"""Test file for the function calls python file."""

import unittest
from src.function_calls import OPTFunction

class TestOPTFunction(unittest.TestCase):
    def setUp(self):
        self.opt_function = OPTFunction()
        self.oddList = []
        self.evenList = []

    def test_optimized_function(self):
        self.opt_function.optimized_function(self.oddList, self.evenList)
        self.assertEqual(len(self.oddList), 100000)  # 10 odd numbers * 10000
        self.assertEqual(len(self.evenList), 100000)  # 10 even numbers * 10000
        self.assertTrue(all(i % 2 != 0 for i in self.oddList))
        self.assertTrue(all(i % 2 == 0 for i in self.evenList))

if __name__ == "__main__":
    unittest.main()
