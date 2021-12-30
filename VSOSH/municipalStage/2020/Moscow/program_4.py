N = int(input())
M = int(input())

a = list(map(lambda x: -x, [int(input()) for _ in range(N)]))
b = [int(input()) for _ in range(M)]

print(max(sorted(a+b)[(N+M) // 2], 0))
