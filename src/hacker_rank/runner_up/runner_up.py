def runner_up():
    _ = int(input())
    arr = map(int, input().split())
    fst = -100
    snd = -100
    for i in arr:
        if i > fst:
            snd = fst
            fst = i
        elif i < fst and i > snd:
            snd = i
    print(snd)
