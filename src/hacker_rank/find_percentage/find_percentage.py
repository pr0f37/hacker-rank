def find_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s_m = student_marks[query_name]
    print(f"{sum(s_m) / len(s_m):.2f}")
