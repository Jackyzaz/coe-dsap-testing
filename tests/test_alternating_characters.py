from program.alternating_characters import alternatingCharacters
import unittest


class AlternatingCharactersTest(unittest.TestCase):
    # case 1: min length
    def test_give_A_will_return_0(self):
        # arrange
        test_case = "A"
        expected_output = 0

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 2: above min length by 1
    def test_give_AA_will_return_1(self):
        # arrange
        test_case = "AA"
        expected_output = 1

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 3: above min length by 1
    def test_give_AB_will_return_0(self):
        # arrange
        test_case = "AB"
        expected_output = 0

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 4: average case
    def test_give_ABABABAB_will_return_2(self):
        # arrange
        test_case = "ABABABAB"
        expected_output = 0

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 5: average case
    def test_give_AAAAAAAA_will_return_2(self):
        # arrange
        test_case = "AAAAAAAA"
        expected_output = 7

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 6: max case return 4999
    def test_give_A_5000_will_return_4999(self):
        # arrange
        test_case = "A" * 5000
        expected_output = 4999

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 7: max case return 0
    def test_give_AB_5000_will_return_0(self):
        # arrange
        test_case = "AB" * 5000
        expected_output = 0

        # act
        result = alternatingCharacters(test_case)

        # assert
        self.assertEqual(result, expected_output)
