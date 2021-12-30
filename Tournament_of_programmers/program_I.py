n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

a, b, c = map(int, input().split())

if list(set(g[a]) & set(g[b]) & set(g[c])) == 1:
    print('YES')
else:
    print('NO')
