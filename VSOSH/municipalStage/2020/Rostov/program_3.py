from bisect import bisect_right

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))
k = int(input())

ans = 0
for i in range(len(a)):
    ans += bisect_right(b, k-a[i])

print(ans)