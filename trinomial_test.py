import unittest
from trinomial import *

class Trinomial_function_test(unittest.TestCase):

    def test_all_zeros(self):
        assert trinomial(0, 0, 0) == None

    def test_all_ones(self):
        assert trinomial(1, 1, 1) == ()

    def test_invalid_argument_1(self):
        assert trinomial("a", 2, 8) == None

    def test_invalid_argument_2(self):
        assert trinomial(25,77,[1,2]) == None

    def test_no_3_args(self):
        assert trinomial([1,2]) == None
        assert trinomial(1,2,4,7.0) == None

    def test_check_invalid_argumant(self):
        assert check1("aa") == (False, None)
    
    def test_check_correct_case(self):
        assert check1(1,5,3)[0] == True
        assert type(check1(1,5,3)[1]) == tuple


if __name__ == '__main__':
    unittest.main()

