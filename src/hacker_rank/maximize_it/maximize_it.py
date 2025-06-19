import itertools


def calc_func(tup, M) -> int:
    return sum(map(lambda x: x**2, tup)) % M


if __name__ == "__main__":
    K, M = map(int, input().split())
    s = [None for _ in range(M)]
    lists = []
    for _ in range(K):
        _, *lst = map(int, input().split())
        lists.append(lst)

    for tup in itertools.product(*lists):
        s_tup = sum(map(lambda x: x**2, tup)) % M
        if s[s_tup] is None:
            s[s_tup] = tup
        if s[M - 1] is not None:
            break

    for idx, tup in reversed(list(enumerate(s))):
        if tup is not None:
            print(f"{tup} -> {idx}")
            break
