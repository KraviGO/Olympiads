n = int(input())
a = list(map(int, input().split()))
mas = [0] * n
visit = [0] * n
for i in range(n):
    visit[a[i]] += 1
    if visit[a[i]] >= 2:
        visit[a[i]] = 0
        mas[i] = mas[i-1] - 1
    else:
        mas[i] = mas[i-1] + 1

k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    print(max(mas[l-1:r-1]))
