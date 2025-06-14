def nested_lists():
    scores = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        try:
            scores[score].append(name)
        except KeyError:
            scores[score] = [name]

    for n in sorted(scores[sorted(list(scores.keys()))[1]]):
        print(n)
