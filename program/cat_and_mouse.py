"""
x - Cat A position
y - Cat B position
z - Mouse C position
Constraints:
 1 <= x, y, z <=100
"""


def cat_and_mouse(x: int, y: int, z: int) -> str:
    cat_a_diff = abs(x - z)
    cat_b_diff = abs(y - z)
    if cat_a_diff == cat_b_diff:
        return "Mouse C"
    elif cat_a_diff < cat_b_diff:
        return "Cat A"
    elif cat_a_diff > cat_b_diff:
        return "Cat B"


if __name__ == "__main__":
    line_str = input("Enter A B C:")
    line = map(int, line_str.split())
    result = cat_and_mouse(*line)
    print("Result:", result)
