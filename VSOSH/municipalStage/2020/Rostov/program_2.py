def get_best(a):
    return sorted(a, reverse=True, key=lambda x: (sum(x), x[0], x[1], x[2]))[0]


a = [list(map(int, input().split())) + [i + 1] for i in range(2)]
B, C = list(map(int, input().split()))

best = get_best(a)
ans = max(sum(best[:-1]) - B - C, 0)
if a + [ans, B, C, 3] == 3:
    print(ans)
else:
    print(ans + 1)
