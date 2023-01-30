#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "src"))
from functionality import *
import unittest

class Trinomial_function_test(unittest.TestCase):

    def test_no_params(self):
        assert trinomial() == None

    def test_all_ones(self):
        assert trinomial(1, 1, 1) == ()
    
if __name__ == '__main__':
    unittest.main()
