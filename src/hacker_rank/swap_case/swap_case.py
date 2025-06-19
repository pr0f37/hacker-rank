from string import ascii_lowercase, ascii_uppercase


def swap_case(s):
    result = ""
    for char in s:
        if char in ascii_lowercase:
            result += ascii_uppercase[ascii_lowercase.index(char)]
        elif char in ascii_uppercase:
            result += ascii_lowercase[ascii_uppercase.index(char)]
        else:
            result += char
    return result


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
