from program.stub_guess_number import (
    guess_int,
    guess_float,
)
import unittest
from unittest.mock import patch


class TestGuessFunctions(unittest.TestCase):

    # case 1: guess_int with range 1-1
    @patch("random.randint")
    def test_guess_int_1to1(self, mock_randint):
        # arrange
        test_case = (1, 1)
        expected_output = 1
        # mock
        mock_randint.return_value = expected_output

        # act
        result = guess_int(*test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 2: guess_int with range 1-10
    @patch("random.randint")
    def test_guess_int_1to10(self, mock_randint):
        # arrange
        test_case = (1, 10)
        expected_output = 5
        # mock
        mock_randint.return_value = expected_output

        # act
        result = guess_int(*test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 3: guess_float with range 1-1
    @patch("random.uniform")
    def test_guess_float_1to1(self, mock_uniform):
        # arrange
        test_case = (1, 1)
        expected_output = 1
        # mock
        mock_uniform.return_value = expected_output

        # act
        result = guess_float(*test_case)

        # assert
        self.assertEqual(result, expected_output)

    # case 4: guess_float with range 1-10
    @patch("random.uniform")
    def test_guess_float_1to10(self, mock_uniform):
        # arrange
        test_case = (1, 10)
        expected_output = 5.55555
        # mock
        mock_uniform.return_value = expected_output

        # act
        result = guess_float(*test_case)

        # assert
        self.assertEqual(result, expected_output)
