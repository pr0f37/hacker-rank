def split_and_join(line: str):
    return line.replace(" ", "-")


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
