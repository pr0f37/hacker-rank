import re


def find_postal_code(P: str):
    regex_integer_in_range = r"^[1-9]\d{5}$"

    return bool(re.match(regex_integer_in_range, P))


def find_alt_pair(P: str):
    regex_alternating_repetitive_digit_pair = r"(?P<left>\d)(?=(\d)(?P=left))"

    return len(re.findall(regex_alternating_repetitive_digit_pair, P))


def test():
    assert find_postal_code("100000") is True, "Test failed!"
    assert find_postal_code("200000") is True, "Test failed!"
    assert find_postal_code("999999") is True, "Test failed!"
    assert find_postal_code("10000") is False, "Test failed!"
    assert find_postal_code("1000000") is False, "Test failed!"
    assert find_postal_code("000001") is False, "Test failed!"


def test_2():
    print(find_alt_pair("110000"))


if __name__ == "__main__":
    test()
    test_2()
