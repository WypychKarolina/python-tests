
import unittest
from trinomial import *

class Trinomial_function_test(unittest.TestCase):

    def test_all_zeros(self):
        assert trinomial(0, 0, 0) == None

    def test_all_ones(self):
        assert trinomial(1, 1, 1) == ()
    
if __name__ == '__main__':
    unittest.main()
