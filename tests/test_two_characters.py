from program.two_characters import two_characters
import unittest


class TwoCharactersTest(unittest.TestCase):
    # case 1: min length character
    def test_give_a_is_0(self):
        # arrange
        test_case = "a"
        expected_output = 0

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 2: above min length character by 1 (same character)
    def test_give_aa_is_0(self):
        # arrange
        test_case = "aa"
        expected_output = 0

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 3: above min length character by 1 (distinct character)
    def test_give_ab_is_b(self):
        # arrange
        test_case = "ab"
        expected_output = 2

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 4: average case all is unique character
    def test_give_abcde_is_2(self):
        # arrange
        test_case = "abcde"
        expected_output = 2

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 5: long character with same pattern
    def test_give_abababababababababababab_is_24(self):
        # arrange
        test_case = "abababababababababababab"
        expected_output = 24

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 6: long character with repeats block
    def test_give_aaaaabbbbbxxxxxyyyyy_is_0(self):
        # arrange
        test_case = "aaaaabbbbbxxxxxyyyyy"
        expected_output = 0

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 7: very long big character but no alternating
    def test_give_a1000b1000_is_0(self):
        # arrange
        test_case = "a" * 1000 + "b" * 1000
        expected_output = 0

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 8: very long with alterating
    def test_give_ab1000_is_2000(self):
        # arrange
        test_case = "ab" * 1000
        expected_output = 2000

        # act
        result = two_characters(test_case)

        # assert
        self.assertEqual(result, expected_output)
