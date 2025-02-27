from program.funny_string import funny_string
import unittest

FUNNY = "Funny"
NOT_FUNNY = "Not Funny"


class FunnyStringTest(unittest.TestCase):
    # case 1: min length analysis (min is 1 character)
    def test_give_A_is_funny(self):
        # arrange
        test_case = "A"
        expected_output = FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 2: near min length analysis (near min is 2 character)
    def test_give_NA_is_funny(self):
        # arrange
        test_case = "NA"
        expected_output = FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 3: average string case funny
    def test_give_lmnop_is_funny(self):
        # arrange
        test_case = "lmnop"
        expected_output = FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 4: average string case not funny
    def test_give_amnop_is_not_funny(self):
        # arrange
        test_case = "amnop"
        expected_output = NOT_FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 5: near max length (kinda palindome)
    def test_give_abcdefghijklmzyxwvutsrqpon_is_funny(self):
        # arrange
        test_case = "abcdefghijklmzyxwvutsrqpon"
        expected_output = FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 6: max length (kinda palindome)
    def test_give_abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba_is_funny(self):
        # arrange
        test_case = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
        expected_output = FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 7: weird case duplicate string
    def test_give_aabbcc_is_funny(self):
        # arrange
        test_case = "aabbcc"
        expected_output = FUNNY

        # act
        result = funny_string(test_case)

        # assert
        self.assertEqual(result, expected_output)
