from program.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    # case 1: empty list
    def test_give_empty_list_is_not_prime(self):
        prime_list = []
        self.assertFalse(is_prime_list(prime_list))

    # case 2: Negative Number Boundary
    def test_give_negative_3_2_1_is_not_prime(self):
        prime_list = [-3, -2, -1]
        self.assertFalse(is_prime_list(prime_list))

    # case 3: 0 is not prime
    def test_give_negative_0_is_not_prime(self):
        prime_list = [0]
        self.assertFalse(is_prime_list(prime_list))

    # case 4: 1 is not prime
    def test_give_1_is_not_prime(self):
        prime_list = [1]
        self.assertFalse(is_prime_list(prime_list))

    # case 5: average prime number
    def test_give_19_29_37_47_59_67_79_is_prime_list(self):
        prime_list = [19, 29, 37, 47, 59, 67, 79]
        self.assertTrue(is_prime_list(prime_list))

    # case 6: Big non-prime number
    def test_give_1111111_is_not_prime(self):
        prime_list = [1_111_111]
        self.assertFalse(is_prime_list(prime_list))

    # case 7: Big prime number
    # ChatGPT said 999,983 is the most biggest 6-digits number that this alogrithmn can calculate in 10 seconds
    # (actually depend on your computer)
    def test_give_999999999999999989_is_prime(self):
        prime_list = [999_983]
        self.assertTrue(is_prime_list(prime_list))
