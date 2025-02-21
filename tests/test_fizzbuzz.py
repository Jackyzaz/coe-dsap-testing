from program.fizzbuzz import fizzbuzz
import unittest


FIZZBUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"


class FizzBuzzTest(unittest.TestCase):

    # case 1: Negative number is Fizz
    def test_give_minus_3_6_9_is_Fizz(self):
        test_cases = [-3, -6, -9]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), FIZZ)

    # case 2: Negative number is Buzz
    def test_give_minus_5_10_20_is_Buzz(self):
        test_cases = [-5, -10, -20]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), BUZZ)

    # case 3: Negative number is FizzBuzz
    def test_give_minus_15_30_45_is_FizzBuzz(self):
        test_cases = [-15, -30, -45]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), FIZZBUZZ)

    # case 4: Positive number is Fizz
    def test_give_3_6_9_is_Fizz(self):
        test_cases = [3, 6, 9]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), FIZZ)

    # case 5: Postitive number is Buzz
    def test_give_5_10_20_is_Buzz(self):
        test_cases = [5, 10, 20]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), BUZZ)

    # case 6: Positive number is FizzBuzz
    def test_give_15_30_45_is_FizzBuzz(self):
        test_cases = [15, 30, 45]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), FIZZBUZZ)

    # case 7: Boundary number
    # Anything mod 0 will be 0 so its is FizzBuzz
    def test_give_0_is_FizzBuzz(self):
        self.assertEqual(fizzbuzz(0), FIZZBUZZ)

    # case 8: Others wise should return its self
    def test_give_1_2_14_16_29_31_101_103(self):
        test_cases = [1, 2, 14, 16, 29, 31, 101, 103]
        for t in test_cases:
            with self.subTest(t=t):
                self.assertEqual(fizzbuzz(t), t)
