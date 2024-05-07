import unittest
from pycot_src.parallel_processing_simple import pool_second_power, pool_third_power

class TestParallelProcessingSimple(unittest.TestCase):

    def test_pool_second_power(self):
        self.assertEqual(pool_second_power(2), 4)
        self.assertEqual(pool_second_power(3), 9)
        self.assertEqual(pool_second_power(4), 16)

    def test_pool_third_power(self):
        self.assertEqual(pool_third_power(2), 8)
        self.assertEqual(pool_third_power(3), 27)
        self.assertEqual(pool_third_power(4), 64)

if __name__ == '__main__':
    unittest.main()
