from program.caesar_cipher import caesar_cipher
import unittest


class CaesarCipherTest(unittest.TestCase):
    # case 1: min length and min k
    def test_give_a_1_is_b(self):
        # arrange
        test_case = ["a", 1]
        expected_output = "b"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 2: above min by 1
    def test_give_ab_2_is_cd(self):
        # arrange
        test_case = ["ab", 2]
        expected_output = "cd"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 3: Test average case without k rotate
    def test_give_hello_2_is_jgnnq(self):
        # arrange
        test_case = ["hello", 2]
        expected_output = "jgnnq"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 4: Test average case with k rotate
    def test_give_hello_13_is_uryyb(self):
        # arrange
        expected_output = "uryyb"
        test_case = ["hello", 13]
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 5: Max case
    def test_give_abcdefghijklmnopqrstuvwxyz_13_is_nopqrstuvwxyzabcdefghijklm(self):
        # arrange
        test_case = ["abcdefghijklmnopqrstuvwxyz", 13]
        expected_output = "nopqrstuvwxyzabcdefghijklm"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 6: weird case k = 0
    def test_give_unchanged_0_is_unchanged(self):
        # arrange
        test_case = ["unchanged", 0]
        expected_output = "unchanged"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 7: weird case k = 26 its will be same place
    def test_give_same_25_is_same(self):
        # arrange
        test_case = ["same", 26]
        expected_output = "same"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 8: Mixed and Upper and Lower
    def test_give_HelloWorld_13_is_UryybJbeyq(self):
        # arrange
        test_case = ["HelloWorld", 13]
        expected_output = "UryybJbeyq"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)

    # case 9: Special Character
    def test_give_special_13_is_special(self):
        # arrange
        test_case = ["$%!%$@", 13]
        expected_output = "$%!%$@"
        # act
        result = caesar_cipher(*test_case)
        # assert
        self.assertEqual(result, expected_output)
