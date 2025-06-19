import re


def decrypt(matrix: list[str], n: int, m: int) -> str:
    s = "".join(matrix[x][y] for y in range(m) for x in range(n))
    result = re.sub(r"(\w)\W+(\w)", r"\g<1> \g<2>", s)
    return result


def test(matrix: list[str], expected: str):
    n = len(matrix)
    m = len(matrix[0])
    result = decrypt(matrix, n, m)

    assert result == expected, f"Expected: {expected}, but got: {result}"


if __name__ == "__main__":
    matrix = [
        "Tsi",
        "h%x",
        "i #",
        "sM ",
        "$a ",
        "#t%",
        "ir!",
    ]
    test(matrix, "This is Matrix#  %!")  # Example test case
