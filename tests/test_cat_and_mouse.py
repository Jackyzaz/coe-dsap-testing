from program.cat_and_mouse import cat_and_mouse
import unittest
from unittest.mock import patch

CAT_A = "Cat A"
CAT_B = "Cat B"
MOUSE_C = "Mouse C"


class CatAndMouseTest(unittest.TestCase):
    # case 1: Min-Boundary when 3 are overlapping for Mouse
    def test_give_1_1_1_is_Mouse_C(self):
        test_case = [1, 1, 1]
        expected_ouput = MOUSE_C

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_ouput)

    # case 2: Min-Boundary when cat are equal dif for Mouse
    def test_give_50_50_1_is_Mouse_C(self):
        test_case = [50, 50, 1]
        expected_output = MOUSE_C

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)

    # case 3: Middle-Value Case Mouse
    def test_give_1_99_50_is_Mouse_C(self):
        test_case = [1, 99, 50]
        expected_output = MOUSE_C

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)

    # case 4: Max-Boundary where everyone is same position
    def test_give_100_100_100_is_Mouse_C(self):
        test_case = [100, 100, 100]
        expected_output = MOUSE_C

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)

    # case 5: Cat A win At Boundary dif 1
    def test_give_1_4_2_is_Cat_A(self):
        test_case = [1, 4, 2]
        expected_output = CAT_A

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)

    # case 6: Cat A win At same position with Mouse C
    def test_give_1_100_1_is_Cat_A(self):
        test_case = [1, 100, 1]
        expected_output = CAT_A

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)

    # case 7: Cat B win At Boundary dif 1
    def test_give_1_2_3_is_Cat_B(self):
        test_case = [1, 2, 3]
        expected_output = CAT_B

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)

    # case 8: Cat B win At same position with Mouse C
    def test_give_1_50_50_is_Cat_B(self):
        test_case = [1, 50, 50]
        expected_output = CAT_B

        result = cat_and_mouse(*test_case)

        self.assertEqual(result, expected_output)
