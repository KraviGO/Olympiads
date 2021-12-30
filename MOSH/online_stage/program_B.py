N, T = map(int, input().split())
W = list(sorted(zip(list(map(int, input().split())), list(range(1, N+1)))))
M = sorted(list(map(lambda x: (x[1] - x[0]*T, x[2]), zip((map(int, input().split())), list(map(int, input().split())), list(range(N))))))

ans = [0] * N
for i in range(N):
    ans[M[i][1]] = W[i][1]

print(*ans)
