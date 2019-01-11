import unittest

# https://docs.python.org/3.4/library/operator.html
class TestOperator(unittest.TestCase):

# https://introcs.cs.princeton.edu/python/12types/
# Why does 10^6 evaluate to 12 instead of 1000000?
    def test_bitwise_xor(self):
        self.assertEqual(10^6,12)
        # why?
        # ^ is bitwise exclusive or (xor):
        self.assertEqual( '0b110',bin(6))
        self.assertEqual('0b1010',bin(10))
        # exclusive bitwise or:
        self.assertEqual('0b1100',bin(12))


if __name__ == '__main__':
    unittest.main()
