from program.grid_challenge import grid_challenge
import unittest

YES = "YES"
NO = "NO"


class GridChallengeTest(unittest.TestCase):
    # case 1: min size 1x1 (single character)
    def test_give_a_is_yes(self):
        # arrange
        test_case = ["a"]
        expected_output = YES

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 2: min size 2x2
    def test_give_ab_cd_is_yes(self):
        # arrange
        test_case = ["ab", "cd"]
        expected_output = YES

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 3: min size 2x2 but not valid
    def test_give_xy_ab_is_no(self):
        # arrange
        test_case = ["xy", "ab"]
        expected_output = NO

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 4: average case with yes
    def test_give_abc_hij_xyz_is_yes(self):
        # arrange
        test_case = ["abc", "hij", "xyz"]
        expected_output = YES

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 5: average case with no
    def test_give_xyz_hij_abc_is_no(self):
        # arrange
        test_case = ["xyz", "hij", "abc"]
        expected_output = NO

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 6: grid all same
    def test_give_aaa_aaa_aaa_is_yes(self):
        # arrange
        test_case = ["aaa", "aaa", "aaa"]
        expected_output = YES

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 7: large grid case
    def test_give_50row_abc___xyz_is_yes(self):
        # arrange
        test_case = [
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx",
        ]

        expected_output = YES

        # act
        result = grid_challenge(test_case)

        # assert
        self.assertEqual(result, expected_output)
